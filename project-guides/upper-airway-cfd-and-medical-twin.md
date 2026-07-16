# Upper-Airway CFD and Medical Digital Twin

## Goal

Connect patient-specific airway geometry and breathing conditions to pressure/velocity behavior, reduced-order representations, and diagnostic indicators.

## Repository roles

| Repository | Role |
|---|---|
| [ML-foundations](https://github.com/jonkrohn/ML-foundations) | Linear algebra, statistics, and ML prerequisites |
| [CFDPython](https://github.com/barbagroup/CFDPython) | Governing-equation and discretization foundation |
| [ml-cfd-lecture](https://github.com/AndreWeiner/ml-cfd-lecture) | ML–CFD integration |
| [PyDMD](https://github.com/PyDMD/PyDMD) | Classical ROM baseline |
| [Awesome-AI4CFD](https://github.com/WillDreamer/Awesome-AI4CFD) | Literature and method discovery |
| [PINNs](https://github.com/maziarraissi/PINNs) | Physics-informed alternatives |

## Suggested workflow

1. Validate patient-specific CFD against available experimental or clinical evidence.
2. Export consistent pressure and velocity snapshots.
3. Standardize mesh mapping, probes, or sampling locations.
4. Build POD/DMD baselines.
5. Train an autoencoder and inspect latent dimension sensitivity.
6. Introduce linear latent evolution for Koopman-style prediction.
7. Compare DMD, CNN-AE, and CNN-KAE using identical data splits.
8. Relate reduced variables and reconstructed fields to clinical indices.
9. Report uncertainty, failure cases, and generalization limits.
