# Resource Selection Guide

[← Resource library](./README.md) · [Main hub](../README.md)

Use this page to choose a tool based on the research task rather than popularity.

## Numerical CFD

| Need | Start with | Move to |
|---|---|---|
| Learn discretization from equations | CFDPython | FiPy or a small educational solver |
| Study production finite-volume workflows | OpenFOAM-dev | Solver customization and benchmark cases |
| Compressible CFD and adjoint design | SU2 | Shape optimization and multiphysics design |
| Custom variational PDE formulation | DOLFINx | Coupled or nonlinear finite-element models |

## Geometry, mesh, and post-processing

| Need | Recommended resource |
|---|---|
| Scripted mesh generation | Gmsh |
| Convert between mesh formats | meshio |
| Interactive CFD visualization | ParaView |
| Automated Python post-processing | PyVista |

## Verification and validation

| Need | Recommended resource |
|---|---|
| Verify RANS turbulence-model implementation | NASA Turbulence Modeling Resource |
| Select classic experimental validation cases | ERCOFTAC Classic Collection |
| Query high-fidelity turbulence fields | JHTDB through Giverny |

## Reduced-order modeling and scientific AI

| Need | Start with | Compare against |
|---|---|---|
| DMD or Koopman baseline | PyDMD | flowTorch |
| Physics-structured non-intrusive ROM | Operator Inference | PyDMD and full-order CFD |
| Sparse governing-equation discovery | PySINDy | Known equations and held-out trajectories |
| PINN or DeepONet experiments | DeepXDE | Numerical solver baseline |
| Fourier Neural Operator | NeuralOperator | U-Net, autoregressive, and classical surrogate baselines |
| Standard SciML benchmark | PDEBench | PDEArena implementations |
| Differentiable CFD | JAX-Fluids or PhiFlow | Conventional CFD and finite-difference checks |
| Scalable physics-AI training | PhysicsNeMo | Smaller transparent baseline first |

## Engineering design

| Need | Recommended resource |
|---|---|
| Multi-objective optimization | pymoo |
| Kriging, RBF, DOE, and multifidelity surrogates | SMT |
| Adjoint aerodynamic design | SU2 |

## Application-specific workflows

| Application | Recommended route |
|---|---|
| Medical image to CFD geometry | 3D Slicer → VMTK or SimVascular |
| PIV processing | OpenPIV or PIVlab → flowTorch → PyDMD |
| Partitioned FSI | Independently verified solvers → preCICE |
| Cavitation image analysis | BubbleID plus validated multiphase CFD |
