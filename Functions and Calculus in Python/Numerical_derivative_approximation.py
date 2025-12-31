# Challenge 2: 
# Approximate the derivative of sin(x) at x = π/4 using the math.sin function 
# (only math allowed). Compare with the exact value cos(π/4) ≈ 0.707.


# Objective: 
# Implement the concept of a derivative using the limit definition: 
# f′(x)=lim⁡h→0f(x+h)−f(x)hf′(x)=h→0limhf(x+h)−f(x) 

import math

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# sin(x) ka derivative at pi/4
x = math.pi / 4

approx_derivative = derivative(math.sin, x)
exact_value = math.cos(x)

print("Approximate derivative:", approx_derivative)
print("Exact value (cos(pi/4)):", exact_value)
