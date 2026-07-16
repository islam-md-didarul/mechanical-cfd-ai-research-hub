# Reduced-Order Modeling

## Objective

Represent high-dimensional transient flow data with compact models while retaining dominant spatial and temporal behavior.

## Recommended progression

1. Linear algebra and Singular Value Decomposition
2. Proper Orthogonal Decomposition
3. [PyDMD/PyDMD](https://github.com/PyDMD/PyDMD)
4. Extended, optimized, or controlled DMD
5. Koopman operator concepts
6. Autoencoders and convolutional autoencoders
7. Linear latent dynamics and CNN-KAE
8. [maziarraissi/PINNs](https://github.com/maziarraissi/PINNs) for physics-constrained alternatives

## Validation checklist

- Reconstruction error
- Multi-step prediction error
- Stability of latent dynamics
- Generalization to unseen cases
- Physical plausibility and conservation
- Comparison with DMD/POD baselines
- Computational speed-up
