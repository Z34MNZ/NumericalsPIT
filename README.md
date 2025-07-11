# 📐 Newton-Raphson Method Calculator (Streamlit App)

This interactive calculator allows users to solve nonlinear equations of the form `f(x) = 0` using the **Newton-Raphson Method**. Built with Python and Streamlit, it provides step-by-step iteration outputs, error tracking, and convergence visualization.

---

## 📘 Overview

The **Newton-Raphson Method** is an efficient root-finding algorithm that approximates a solution to a nonlinear equation by iteratively improving an initial guess. Given a differentiable function `f(x)`, the method applies the update formula:

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

It is especially useful when a good initial approximation is known and the function is smooth.

---

## 🧮 Features

- Accepts user input for:
  - Function `f(x)`
  - Initial guess `x₀`
  - Tolerance
  - Maximum number of iterations
- Automatically computes the derivative using symbolic differentiation
- Displays:
  - Iteration table (x, f(x), f'(x), next x, error)
  - Final root approximation
  - Convergence plot of errors across iterations
- Handles invalid input and potential divergence (e.g., zero derivative)

---
