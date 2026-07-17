#!/usr/bin/env python3
"""Validate the machine-readable resource catalog."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from urllib.parse import urlparse
import sys

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required: python -m pip install pyyaml") from exc


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "resources" / "catalog.yml"
REQUIRED_RESOURCE_FIELDS = {
    "name",
    "url",
    "category",
    "type",
    "level",
    "priority",
    "summary",
    "best_for",
}
ALLOWED_PRIORITIES = {"core", "supporting", "specialized", "reference", "optional"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))

    if data.get("schema_version") != 2:
        fail("schema_version must be 2")

    hub = data.get("hub", {})
    categories = data.get("categories", [])
    resources = data.get("resources", [])

    category_ids = [item.get("id") for item in categories]
    if not category_ids or None in category_ids:
        fail("every category requires an id")
    if len(category_ids) != len(set(category_ids)):
        fail("duplicate category ids detected")

    category_set = set(category_ids)
    names = []
    urls = []

    for index, resource in enumerate(resources, start=1):
        missing = REQUIRED_RESOURCE_FIELDS - set(resource)
        if missing:
            fail(f"resource #{index} is missing: {sorted(missing)}")

        if resource["category"] not in category_set:
            fail(f"{resource['name']}: unknown category {resource['category']}")

        if resource["priority"] not in ALLOWED_PRIORITIES:
            fail(f"{resource['name']}: invalid priority {resource['priority']}")

        parsed = urlparse(resource["url"])
        if parsed.scheme != "https" or not parsed.netloc:
            fail(f"{resource['name']}: URL must be a valid HTTPS URL")

        if len(resource["summary"].strip()) < 30:
            fail(f"{resource['name']}: summary is too short")
        if len(resource["best_for"].strip()) < 20:
            fail(f"{resource['name']}: best_for is too short")

        names.append(resource["name"].casefold())
        urls.append(resource["url"].rstrip("/").casefold())

    duplicate_names = [name for name, count in Counter(names).items() if count > 1]
    duplicate_urls = [url for url, count in Counter(urls).items() if count > 1]
    if duplicate_names:
        fail(f"duplicate resource names: {duplicate_names}")
    if duplicate_urls:
        fail(f"duplicate resource URLs: {duplicate_urls}")

    if hub.get("resource_count") != len(resources):
        fail(
            f"hub.resource_count={hub.get('resource_count')} "
            f"but catalog contains {len(resources)} resources"
        )

    actual_counts = Counter(item["category"] for item in resources)
    for category in categories:
        expected = category.get("resource_count")
        actual = actual_counts[category["id"]]
        if expected != actual:
            fail(
                f"{category['id']}: resource_count={expected}, "
                f"actual={actual}"
            )

    print(
        f"Catalog valid: {len(resources)} resources, "
        f"{len(categories)} categories, no duplicate names or URLs."
    )



if __name__ == "__main__":
    main()
