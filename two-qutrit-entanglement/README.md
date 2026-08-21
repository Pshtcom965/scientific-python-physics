# Geometric and Operational Characterization of Two-Qutrit Entanglement

## Overview

This repository contains the numerical analysis and visualization associated with my research on the geometric and operational characterization of bipartite two-qutrit pure-state entanglement.

The project studies the entanglement structure of two-qutrit states through the eigenvalues of the reduced density matrix and complementary entanglement invariants.

## Computational Analysis

The numerical implementation includes:

- Generation of random two-qutrit pure states
- Construction of the coefficient matrix and reduced density matrix
- Calculation of eigenvalues of the reduced density matrix
- Evaluation of the I-concurrence
- Evaluation of the determinant-based geometric invariant G
- Numerical verification of the physical constraint in the (C_I, G) plane
- Visualization of rank-2 and rank-3 entangled states
- Numerical analysis of conditional visibility and predictability in a qutrit quantum-erasure protocol

## Key Quantities

For a two-qutrit pure state with coefficient matrix C,

    rho_A = C C†

The I-concurrence is calculated from the reduced density matrix as

    C_I = sqrt(2(1 - Tr(rho_A^2)))

The normalized determinant-based geometric invariant is

    G = 3 sqrt(3) sqrt(lambda_1 lambda_2 lambda_3)

where lambda_1, lambda_2, and lambda_3 are the eigenvalues of the reduced density matrix.

The numerical results demonstrate the physically accessible region of two-qutrit states in the (C_I, G) plane.

## Numerical Results

Randomly generated two-qutrit pure states are used to verify the analytic constraint between C_I and G.

The numerical analysis distinguishes:

- Rank-2 states, for which G = 0
- Rank-3 states, for which G > 0

The repository will reproduce the numerical results and scientific visualizations associated with the study.

## Tools

- Python
- NumPy
- Matplotlib
- Scientific computing
- Numerical linear algebra

## Associated Publication

**Geometric and Operational Characterization of Two-Qutrit Entanglement**

Ankita Jana

https://doi.org/10.48550/arXiv.2601.06783

## Project Status

Numerical implementation and visualization are being organized as a reproducible scientific-computing project.
