# Differential Equation Analyzer

The **Differential Equation Analyzer** is a Python-based application designed to analyze first-order differential equations. It provides two main functionalities:
1. **Exactness Checker**: Determines whether a given differential equation is exact.
2. **Homogeneity Checker**: Checks if a given differential equation is homogeneous and determines its degree.

The program is built using **PyQt5** for the graphical user interface (GUI), **SymPy** for symbolic mathematics, and **PyInstaller** for compiling the program into a standalone executable.

---

## Features

- **Exactness Checker**:
  - Input: Two mathematical functions, `M(x, y)` and `N(x, y)`.
  - Output: Determines if the equation `M(x, y)dx + N(x, y)dy` is exact.

- **Homogeneity Checker**:
  - Input: Two mathematical functions, `M(x, y)` and `N(x, y)`.
  - Output: Determines if the equation is homogeneous and calculates its degree.

- **User-Friendly Interface**:
  - Built using **PyQt5** and designed with **PyQt5 Designer**.
  - Easy-to-navigate pages for exactness and homogeneity checks.

- **Standalone Executable**:
  - Compiled using **PyInstaller** for easy distribution and use.

---

## Prerequisites

Before running the program, ensure you have the following installed:

- **Python 3.7 or higher**
- Required Python libraries:
  ```bash
  pip install PyQt5 sympy PyInstaller