# Biofluids CFD and Digital Twins

[← Project guides](./README.md) · [Main hub](../README.md)

## Research workflow

```mermaid
flowchart LR
    A["CT / MRI"] --> B["Segmentation"]
    B --> C["Geometry Cleaning"]
    C --> D["Mesh"]
    D --> E["Patient-Specific CFD"]
    E --> F["Pressure / Velocity Metrics"]
    F --> G["DMD / OpInf / CNN-KAE"]
    G --> H["Clinical Prediction"]
```

## Recommended resource route

1. [3D Slicer](https://github.com/Slicer/Slicer) for image import, segmentation, and geometry inspection.
2. [VMTK](https://github.com/vmtk/vmtk) when centerlines, vascular surfaces, or vessel-specific geometry tools are needed.
3. [SimVascular](https://github.com/SimVascular/SimVascular) as a reference for complete patient-specific vascular workflows and physiological boundary conditions.
4. [Gmsh](https://github.com/gmsh/gmsh), [meshio](https://github.com/nschloe/meshio), and [PyVista](https://github.com/pyvista/pyvista) for reproducible mesh and geometry processing.
5. [PyDMD](https://github.com/PyDMD/PyDMD), [flowTorch](https://github.com/AndreWeiner/flowtorch), and [Operator Inference](https://github.com/Willcox-Research-Group/rom-operator-inference-Python3) for transparent ROM baselines.
6. [NeuralOperator](https://github.com/neuraloperator/neuraloperator) or [DeepXDE](https://github.com/lululxvi/deepxde) only after a reliable baseline and independent test design exist.

## Minimum evidence to report

- Imaging protocol, slice spacing, and reconstruction resolution
- Segmentation method, operator dependence, and smoothing decisions
- Geometry truncation and inlet/outlet placement
- Mesh and time-step sensitivity
- Patient-specific or physiologically justified boundary conditions
- Flow direction, sign convention, and reference pressure
- Solver benchmark or experimental validation
- Physiological pressure, velocity, resistance, power, or wall metrics
- ROM baseline, independent-patient testing, and leakage prevention
- Clinical relevance, uncertainty, and limitations
