<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/images/research-hub-banner-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/images/research-hub-banner-light.svg">
    <img src="./assets/images/research-hub-banner-light.svg"
         width="100%"
         alt="Mechanical, CFD and Scientific AI Research Hub">
  </picture>
</p>

<h1 align="center">Mechanical, CFD & Scientific AI Research Hub</h1>

<p align="center">
  Structured learning pathways, verified resources and project-oriented guidance
  for computational engineering research.
</p>

<p align="center">
  <a href="./learning-paths/README.md"><strong>Learning Paths</strong></a>
  ·
  <a href="./project-guides/README.md"><strong>Project Guides</strong></a>
  ·
  <a href="./resources/catalog.md"><strong>Resource Catalog</strong></a>
  ·
  <a href="./resources/selection-guide.md"><strong>Selection Guide</strong></a>
  ·
  <a href="./CONTRIBUTING.md"><strong>Contribute</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/islam-md-didarul/mechanical-cfd-ai-research-hub?style=flat-square" alt="Last commit">
  <img src="https://img.shields.io/github/license/islam-md-didarul/mechanical-cfd-ai-research-hub?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/actions/workflow/status/islam-md-didarul/mechanical-cfd-ai-research-hub/link-check.yml?style=flat-square&label=documentation%20check" alt="Documentation check">
  <img src="https://img.shields.io/badge/resources-57-0969DA?style=flat-square" alt="57 resources">
</p>

---

# About this hub

This repository organizes independent open-source resources into coherent pathways for:

- computational fluid dynamics and numerical methods;
- mechanical and aerospace engineering applications;
- machine learning for fluid mechanics;
- Dynamic Mode Decomposition and Koopman-based reduced-order modeling;
- physics-informed and scientific machine learning;
- finite-element, multiphase and image-analysis workflows;
- scientific writing, presentation and research communication.

> [!NOTE]
> This is a navigation and explanation hub. It links to independent upstream repositories rather than copying their source code. Every external project remains governed by its own license.

---

<p><strong>▌ Choose your pathway</strong></p>

<table>
<tr>
<td width="33%" valign="top" align="center">
  <img src="./assets/icons/foundations.svg" width="72" alt="Foundations icon"><br>
  <p align="center"><strong>Build foundations</strong></p>
  Mathematics, Python, numerical methods, and machine-learning prerequisites.<br><br>
  <a href="./learning-paths/foundations.md"><strong>Start learning →</strong></a>
</td>
<td width="33%" valign="top" align="center">
  <img src="./assets/icons/cfd.svg" width="72" alt="CFD icon"><br>
  <p align="center"><strong>Develop engineering models</strong></p>
  CFD, FEA, meshing, multiphase flow, verification, validation, and engineering applications.<br><br>
  <a href="./learning-paths/cfd.md"><strong>Explore CFD →</strong></a>
</td>
<td width="33%" valign="top" align="center">
  <img src="./assets/icons/scientific-ai.svg" width="72" alt="Scientific AI icon"><br>
  <p align="center"><strong>Apply scientific AI</strong></p>
  DMD, Koopman models, PINNs, neural operators, surrogates, and AI4CFD.<br><br>
  <a href="./learning-paths/scientific-ai.md"><strong>Explore Scientific AI →</strong></a>
</td>
</tr>
</table>

---

<p><strong>▌ Research learning roadmap</strong></p>

```mermaid
flowchart LR
    A["Foundations<br/>Mathematics + Python"]
    B["Numerical Engineering<br/>Discretization + CFD"]
    C["Data Foundations<br/>Machine Learning"]
    D["Credible Simulation<br/>Mesh + V&V"]
    E["Scientific AI<br/>PINNs + Neural Operators"]
    F["Reduced Models<br/>DMD + OpInf + SINDy"]
    G["Research Systems<br/>Surrogates + Digital Twins"]
    H["Communication<br/>Papers + Presentations"]

    A --> B
    A --> C
    B --> D
    C --> E
    D --> F
    E --> F
    F --> G
    D --> G
    G --> H

    classDef foundation fill:#102A43,stroke:#22B8CF,color:#F8FAFC,stroke-width:2px;
    classDef engineering fill:#123B5D,stroke:#4CC9F0,color:#F8FAFC,stroke-width:2px;
    classDef ai fill:#123F3B,stroke:#20C997,color:#F8FAFC,stroke-width:2px;
    classDef output fill:#49351D,stroke:#F4A261,color:#F8FAFC,stroke-width:2px;

    class A foundation;
    class B,D engineering;
    class C,E,F ai;
    class G,H output;
```

<p align="center">
  <a href="./learning-paths/README.md"><strong>View the complete learning paths →</strong></a>
</p>

---

<p><strong>▌ Featured research pathways</strong></p>

<table>
<tr>
<td width="50%" valign="top">
  <p align="center"><img src="./assets/icons/medical-cfd.svg" width="80" alt="Medical CFD icon"></p>
  <p align="center"><strong>Medical CFD & Digital Twins</strong></p>
  <p align="center">CT/MRI → segmentation → geometry → patient-specific CFD → physiological metrics → ROM → prediction</p>
  <p align="center"><a href="./project-guides/medical-cfd.md"><strong>Explore pathway →</strong></a></p>
</td>
<td width="50%" valign="top">
  <p align="center"><img src="./assets/icons/turbomachinery.svg" width="80" alt="Turbomachinery icon"></p>
  <p align="center"><strong>Turbomachinery Optimization</strong></p>
  <p align="center">CAD → mesh independence → RANS/URANS → experiment → surrogate → multi-objective optimization</p>
  <p align="center"><a href="./project-guides/turbomachinery.md"><strong>Explore pathway →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <p align="center"><img src="./assets/icons/piv-rom.svg" width="80" alt="PIV and ROM icon"></p>
  <p align="center"><strong>PIV & Reduced-Order Modeling</strong></p>
  <p align="center">Images or snapshots → preprocessing → POD/DMD → Operator Inference → reconstruction and prediction</p>
  <p align="center"><a href="./project-guides/piv-rom.md"><strong>Explore pathway →</strong></a></p>
</td>
<td width="50%" valign="top">
  <p align="center"><img src="./assets/icons/multiphase.svg" width="80" alt="Multiphase icon"></p>
  <p align="center"><strong>Multiphase Flow & Cavitation</strong></p>
  <p align="center">Multiphase CFD → bubble detection → cavitation metrics → validation → AI-assisted prediction</p>
  <p align="center"><a href="./project-guides/multiphase.md"><strong>Explore pathway →</strong></a></p>
</td>
</tr>
</table>

<p align="center">
  <a href="./project-guides/fsi.md"><strong>Solid Mechanics & FSI</strong></a>
  ·
  <a href="./project-guides/verification-validation.md"><strong>Verification & Validation</strong></a>
  ·
  <a href="./project-guides/surrogate-optimization.md"><strong>Surrogate Modeling & Optimization</strong></a>
</p>

---

<p><strong>▌ Resource collections</strong></p>

<div align="center">

| Collection | Resources | Primary purpose |
|---|---:|---|
| Research Practice & Engineering Maps | 3 | Research planning and multidisciplinary engineering maps |
| Mathematics & Programming Foundations | 4 | Python, mathematics, and numerical prerequisites |
| Machine Learning & AI | 5 | Data-driven modeling and AI foundations |
| CFD Foundations & Numerical Solvers | 10 | Numerical CFD, production solvers, and fluid mechanics |
| Meshing, Post-processing & Data Interchange | 4 | Reproducible mesh generation, conversion, and analysis |
| Verification, Validation & Benchmark Data | 3 | Turbulence-model verification and benchmark datasets |
| Scientific AI, ROM & Differentiable Physics | 15 | DMD, OpInf, SINDy, PINNs, neural operators, and differentiable CFD |
| Optimization, Surrogates & Uncertainty | 2 | DOE, surrogate modeling, and multi-objective design |
| Biofluids & Medical Modeling | 3 | Segmentation, anatomical geometry, and patient-specific simulation |
| Experimental Flow & Image Analysis | 3 | PIV, bubble detection, and experimental data processing |
| Solid Mechanics & Fluid–Structure Interaction | 3 | FEA, custom PDEs, and partitioned multiphysics coupling |
| Research Communication & Productivity | 2 | Thesis preparation and presentation support |

</div>

<p align="center">
  <a href="./resources/catalog.md"><strong>Browse all 57 verified resources →</strong></a>
  ·
  <a href="./resources/selection-guide.md"><strong>Select tools by research task →</strong></a>
</p>

---

# ▌ Featured core toolkit

<table>
<tr>
<td width="50%" valign="top">

<p><strong>CFDPython</strong></p>

`CORE` `BEGINNER–INTERMEDIATE` `JUPYTER`

Progressive numerical CFD training through the 12 Steps to Navier–Stokes.

**Best for:** Connecting governing equations with Python implementation.  
**Source:** [barbagroup/CFDPython](https://github.com/barbagroup/CFDPython)

</td>
<td width="50%" valign="top">

<p><strong>ML Foundations</strong></p>

`CORE` `BEGINNER–INTERMEDIATE` `JUPYTER`

Mathematics and computer-science foundations for machine learning and reduced-order modeling.

**Best for:** Preparing for DMD, autoencoders, Koopman methods, and PINNs.  
**Source:** [jonkrohn/ML-foundations](https://github.com/jonkrohn/ML-foundations)

</td>
</tr>
<tr>
<td width="50%" valign="top">

<p><strong>PyDMD</strong></p>

`CORE` `INTERMEDIATE–ADVANCED` `PYTHON`

A comprehensive Python library for Dynamic Mode Decomposition methods.

**Best for:** CFD/PIV modal analysis, reconstruction, and ROM benchmarking.  
**Source:** [PyDMD/PyDMD](https://github.com/PyDMD/PyDMD)

</td>
<td width="50%" valign="top">

<p><strong>Awesome AI4CFD</strong></p>

`CORE` `INTERMEDIATE–ADVANCED` `LITERATURE`

A structured survey of machine-learning research for computational fluid dynamics.

**Best for:** Literature reviews, method selection, and proposal development.  
**Source:** [WillDreamer/Awesome-AI4CFD](https://github.com/WillDreamer/Awesome-AI4CFD)

</td>
</tr>
</table>

---

<p><strong>▌ Resource classification</strong></p>

<div align="center">

<table>
  <thead>
    <tr>
      <th align="left">Label</th>
      <th align="left">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"><strong>Core</strong></td>
      <td align="left">Directly supports a principal CFD–AI learning pathway</td>
    </tr>
    <tr>
      <td align="left"><strong>Supporting</strong></td>
      <td align="left">Strengthens prerequisites or implementation ability</td>
    </tr>
    <tr>
      <td align="left"><strong>Specialized</strong></td>
      <td align="left">Intended for a focused method or application</td>
    </tr>
    <tr>
      <td align="left"><strong>Reference</strong></td>
      <td align="left">Primarily used to discover additional resources</td>
    </tr>
    <tr>
      <td align="left"><strong>Optional</strong></td>
      <td align="left">Useful for productivity or communication</td>
    </tr>
  </tbody>
</table>

</div>

---

## ▌ How the hub supports research

```mermaid
flowchart LR
    EXP["Experiments / Clinical Data"]
    CFD["High-Fidelity CFD"]
    ROM["Reduced-Order Model"]
    AI["Scientific AI / Surrogate"]
    DEC["Design or Clinical Decision"]
    COM["Publication and Communication"]

    EXP <--> CFD
    CFD --> ROM
    CFD --> AI
    ROM --> DEC
    AI --> DEC
    DEC --> COM

    classDef data fill:#102A43,stroke:#22B8CF,color:#F8FAFC,stroke-width:2px;
    classDef model fill:#123F3B,stroke:#20C997,color:#F8FAFC,stroke-width:2px;
    classDef output fill:#49351D,stroke:#F4A261,color:#F8FAFC,stroke-width:2px;

    class EXP,CFD data;
    class ROM,AI model;
    class DEC,COM output;
```

---

## ▌ Contributing

Resources should be added only after checking relevance, upstream source, license, maintenance status and suitability for a defined learning or research pathway.

[Read the contribution guide →](./CONTRIBUTING.md)

---

## ▌ License and attribution

The MIT license in this hub applies only to the original organization, descriptions, documentation, scripts and visual assets created for this repository. Every linked repository remains governed by its own upstream license.

[Read the attribution notice →](./NOTICE.md)

---

<p align="center">
  Maintained by <strong>Md. Didarul Islam</strong><br>
  Mechanical Engineering · CFD · Scientific AI
</p>
