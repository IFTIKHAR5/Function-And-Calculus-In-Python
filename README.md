LAB MANUAL: FUNCTIONS AND CALCULUS IN PYTHON
=============================================

Module: Data Science
Language: Python
Programming Style: Functional Programming
Libraries Used: math (only where necessary)

------------------------------------------------------------
PROJECT OVERVIEW
------------------------------------------------------------
This lab manual demonstrates the implementation of fundamental
calculus concepts using pure Python without relying on any
machine learning or scientific libraries.

The objective is to build a strong conceptual foundation in:
- Mathematical functions
- Numerical differentiation
- Numerical integration
- Optimization using gradient descent
- Probability interpretation using area under curves
- Linear regression from scratch

All implementations follow a functional programming approach
with simple, readable, and testable functions.

------------------------------------------------------------
OBJECTIVES
------------------------------------------------------------
- Understand how mathematical functions are represented in Python
- Approximate derivatives using the limit definition
- Approximate definite integrals using Riemann sums
- Implement gradient descent for optimization
- Interpret probability as area under a curve
- Build a simple linear regression model without ML libraries

------------------------------------------------------------
PROJECT STRUCTURE
------------------------------------------------------------

Part 1: Understanding Functions in Python
- Definition and evaluation of mathematical functions
- Example: f(x) = x²
- Challenge: g(x) = 3x + 2

Part 2: Numerical Derivative Approximation
- Derivative using limit definition
- Approximation using small step size (h)
- Examples:
  - f(x) = x²
  - f(x) = x³
- Challenge:
  - Approximate derivative of sin(x) at x = π/4
  - Compare with exact value cos(π/4)

Part 3: Numerical Integration (Riemann Sum)
- Left Riemann sum method
- Approximation of definite integrals
- Examples:
  - ∫ x² dx from 0 to 1
  - ∫ 2x dx from 0 to 3
- Challenge:
  - ∫ (1/x) dx from 1 to 2
  - Compare with exact value ln(2)

Part 4: Gradient Descent (Optimization)
- Implementation of gradient descent algorithm
- Numerical gradient using derivative approximation
- Example:
  - Minimize f(x) = (x − 3)²
- Challenge:
  - Minimize f(x) = x⁴ − 5x² + 6
  - Analyze effect of different learning rates

Part 5: Area Under Curve for Probability Density
- Bell-shaped (normal-like) function
- Interpretation of area as probability
- Normalization using √π
- Challenge:
  - Modify bell curve to f(x) = exp(-(x−1)²)
  - Compute probability from x = 0 to x = 2

Final Project: Linear Regression from Scratch
- Linear model: y = mx + c
- Loss function: Mean Squared Error (MSE)
- Manual computation of gradients:
  - ∂Loss/∂m
  - ∂Loss/∂c
- Optimization using gradient descent
- Dataset:
  x = [1, 2, 3, 4]
  y = [2, 4, 6, 8]
- Verification with analytical solution

------------------------------------------------------------
KEY CONCEPTS COVERED
------------------------------------------------------------
- Functions as first-class objects in Python
- Numerical calculus techniques
- Optimization using gradient descent
- Probability density and normalization
- Core ideas behind machine learning training
- Relationship between calculus and data science

------------------------------------------------------------
REQUIREMENTS
------------------------------------------------------------
- Python 3.x
- No external libraries
- math module allowed where necessary

------------------------------------------------------------
HOW TO RUN
------------------------------------------------------------
1. Ensure Python 3 is installed.
2. Open terminal or command prompt.
3. Navigate to the project directory.
4. Run individual Python files using:

   python filename.py

------------------------------------------------------------
EXPECTED LEARNING OUTCOMES
------------------------------------------------------------
After completing this lab, students will be able to:
- Implement calculus concepts programmatically
- Understand optimization techniques used in ML
- Build intuition for probability distributions
- Develop models without relying on libraries
- Transition smoothly into machine learning concepts

------------------------------------------------------------
ACADEMIC INTEGRITY
------------------------------------------------------------
This work is intended for educational purposes.
Students are encouraged to understand each function
and test with different inputs for better learning.

------------------------------------------------------------
END OF README
============================================================
