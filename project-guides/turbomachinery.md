# Turbomachinery and Pump Optimization

[← Project guides](./README.md) · [Main hub](../README.md)

## Research workflow

```mermaid
flowchart LR
    A["Baseline CAD"] --> B["Parameterized Geometry"]
    B --> C["Mesh Independence"]
    C --> D["RANS / URANS CFD"]
    D --> E["Experimental Validation"]
    E --> F["Performance Metrics"]
    F --> G["Optimization"]
    G --> H["Final Verification"]
```

## Recommended resource route

[CFDPython](https://github.com/barbagroup/CFDPython)  
→ [staggered-grid-lid-driven-cavity](https://github.com/jeddiot/staggered-grid-lid-driven-cavity)  
→ [PyCFD](https://github.com/LukeMcCulloch/PyCFD)  
→ [PyDMD](https://github.com/PyDMD/PyDMD)  
→ [Awesome-AI4CFD](https://github.com/WillDreamer/Awesome-AI4CFD)

## Minimum evidence to report

- Design point and operating range
- Geometry parameters and constraints
- Mesh quality and independence
- Turbulence-model justification
- Experimental uncertainty
- Head, efficiency, power, and cavitation metrics
- Optimization objective and validation of the final design

<!-- documentation-status-refresh: 2026-07-16-green-status-refresh -->
