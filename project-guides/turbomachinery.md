# Turbomachinery and Pump Optimization

[← Project guides](./README.md) · [Main hub](../README.md)

## Research workflow

```mermaid
flowchart LR
    A["Baseline CAD"] --> B["Parameterized Geometry"]
    B --> C["Mesh Independence"]
    C --> D["RANS / URANS CFD"]
    D --> E["Experimental Validation"]
    E --> F["Design of Experiments"]
    F --> G["Surrogate + Optimization"]
    G --> H["Final CFD Verification"]
```

## Recommended resource route

- [Gmsh](https://github.com/gmsh/gmsh) for scripted mesh studies when an open meshing route is appropriate.
- [OpenFOAM-dev](https://github.com/OpenFOAM/OpenFOAM-dev) for general finite-volume turbomachinery exploration.
- [SU2](https://github.com/su2code/SU2) for adjoint methods and shape-design learning.
- [NASA TMR](https://tmbwg.github.io/turbmodels/) for turbulence-model equations and verification.
- [ParaView](https://github.com/Kitware/ParaView) and [PyVista](https://github.com/pyvista/pyvista) for field analysis and automated metrics.
- [SMT](https://github.com/SMTorg/smt) for DOE, kriging, multifidelity, and surrogate modeling.
- [pymoo](https://github.com/anyoptimization/pymoo) for constrained multi-objective optimization.
- [PyDMD](https://github.com/PyDMD/PyDMD) or [flowTorch](https://github.com/AndreWeiner/flowtorch) for unsteady modal analysis.

## Minimum evidence to report

- Design point, speed, fluid properties and operating range
- Geometry variables, bounds, and manufacturing constraints
- Mesh quality, near-wall treatment and independence
- Turbulence-model rationale and rotating-frame method
- Interface settings and convergence of torque, head and efficiency
- Experimental uncertainty and repeatability
- Head, efficiency, power, NPSH, cavitation and loss metrics
- DOE coverage and surrogate cross-validation
- Pareto-front interpretation and decision rule
- High-fidelity verification of every selected optimum
