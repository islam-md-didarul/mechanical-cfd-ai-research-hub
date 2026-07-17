# Contributing

Thank you for helping improve the Mechanical, CFD & Scientific AI Research Hub.

## Resource acceptance criteria

A proposed resource should:

1. have a clear upstream source;
2. have an identifiable license or usage statement;
3. contribute to a defined learning path or project guide;
4. provide substantial educational or research value;
5. avoid duplicating an existing resource without a clear reason;
6. be described accurately without overstating its capabilities;
7. be actively maintained, historically important, or explicitly labeled as a legacy reference;
8. provide a reproducible route to documentation, code, data, or examples.

## Adding a resource

1. Add the resource to `resources/catalog.yml`.
2. Update `resources/catalog.md`.
3. Connect it to at least one learning path or project guide.
4. Update the relevant collection count.
5. Run:

```bash
python -m pip install -r requirements-docs.txt
python scripts/validate_catalog.py
```

6. Check relative and external links.
7. Use a descriptive commit message.

## Suggested pull-request description

- **Resource name:**
- **Upstream source:**
- **Category:**
- **Level:**
- **Classification:** Core / Supporting / Specialized / Reference / Optional
- **Reason for inclusion:**
- **License checked:**
- **Maintenance status checked:**
- **Learning path or project guide updated:**

## Writing style

- Use direct technical language.
- Explain the resource's main benefit and recommended use.
- Separate verified facts from interpretation.
- Do not copy large passages from upstream documentation.
- Avoid promotional claims such as “best” unless the comparison is defined.
- Keep category, level, and priority labels consistent.
