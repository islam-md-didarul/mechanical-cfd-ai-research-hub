# CFD and Numerical Engineering Path

[← Learning paths](./README.md) · [Main hub](../README.md)

## Goal

Connect governing equations, discretization, mesh quality, solver behavior, verification, validation and engineering interpretation.

```mermaid
flowchart LR
    A["Governing Equations"] --> B["Small Numerical Solvers"]
    B --> C["Mesh and Boundary Conditions"]
    C --> D["Production CFD"]
    D --> E["Solution Verification"]
    E --> F["Validation"]
    F --> G["Engineering Application"]
```

## Suggested sequence

| Stage | Recommended resource | Main outcome |
|---|---|---|
| Introductory solver coding | [CFDPython](https://github.com/barbagroup/CFDPython) | Understand discretization through progressive examples |
| Reusable finite-volume PDEs | [FiPy](https://github.com/usnistgov/fipy) | Move from hand-coded equations to a PDE framework |
| Pressure–velocity coupling | [staggered-grid-lid-driven-cavity](https://github.com/jeddiot/staggered-grid-lid-driven-cavity) | Study incompressible coupling and boundary conditions |
| Mesh generation | [Gmsh](https://github.com/gmsh/gmsh) | Produce repeatable meshes using scripts |
| Production finite-volume CFD | [OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev) | Learn case structure, turbulence models and solver customization |
| Compressible flow and design | [SU2](https://github.com/su2code/SU2) | Study aerodynamic CFD, adjoints, and shape optimization |
| Post-processing | [ParaView](https://github.com/Kitware/ParaView) and [PyVista](https://github.com/pyvista/pyvista) | Combine interactive and scripted analysis |
| Turbulence-model verification | [NASA TMR](https://tmbwg.github.io/turbmodels/) | Confirm model definitions and implementation behavior |
| Validation cases | [ERCOFTAC Classic Collection](https://cfd.mace.manchester.ac.uk/ercoftac/) | Compare simulation results with established data |

## Credibility checklist

- State governing equations, assumptions and model limitations.
- Define every inlet, outlet, wall, interface and reference pressure.
- Report mesh metrics and near-wall resolution.
- Perform mesh and time-step sensitivity studies using quantities of interest.
- Report residuals together with conservation and physical monitors.
- Verify turbulence-model definitions against an authoritative source.
- Compare against experiments or established benchmark data.
- Quantify experimental, numerical and model-form uncertainty separately.
- Separate numerical observations from physical interpretation.
