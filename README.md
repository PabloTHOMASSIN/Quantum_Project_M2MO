# Quantum Computing in Finance: Markowitz Portfolio Optimization

This repository explores the application of quantum computing to optimize a portfolio of assets using the **Markowitz portfolio theory**. Specifically, it focuses on the use of the **Quantum Approximate Optimization Algorithm (QAOA)** to solve the portfolio optimization problem in a quantum computing environment. The project aims to explore the potential advantages of quantum algorithms in financial modeling and optimization.

## Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Installation](#installation)
- [Contributor](#contributor)
- [License](#license)

## Overview

The Markowitz portfolio optimization problem involves selecting a portfolio of assets that minimizes risk for a given return or maximizes return for a given risk. This problem is traditionally solved using quadratic programming or other classical optimization methods. However, quantum computing offers the potential for faster and more efficient solutions through algorithms like QAOA.

This project uses QAOA to optimize a Markowitz portfolio by minimizing the portfolio variance (risk) subject to constraints on expected returns. The core goal is to demonstrate how quantum algorithms can be used to solve complex optimization problems in finance.

## Objectives

- Implement the **Markowitz portfolio optimization problem** using classical and quantum methods.
- Apply **Quantum Approximate Optimization Algorithm (QAOA)** to optimize portfolio weights.
- Compare the performance of QAOA with traditional optimization methods such as quadratic programming.
- Analyze the feasibility and advantages of quantum algorithms in financial optimization problems.

## Installation

To run the project, you will need a Python environment with the following dependencies:

### Requirements
- Python 3.x
- [Qiskit](https://qiskit.org) (for quantum programming)
- [NumPy](https://numpy.org)
- [Pandas](https://pandas.pydata.org)
- [Matplotlib](https://matplotlib.org)
- [Scipy](https://scipy.org)

You can install the required packages by running:

```bash
pip install -r requirements.txt
```

## Contributor

THOMASSIN Pablo : pablo.thomassin@etu.u-paris.fr
COZ Olivier : olivier.coz@etu.u-paris.fr
BERDOUS Louiza : louiza.berdous@etu.u-paris.fr

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
