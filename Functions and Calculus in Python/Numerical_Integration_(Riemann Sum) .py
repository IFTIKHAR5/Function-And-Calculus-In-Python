# Challenge 3: 
# Approximate the integral of f(x) = 1/x from 1 to 2 using n=5000 partitions. Compare 
# with the exact value ln(2) ≈ 0.693.


# Objective: 
# Approximate the definite integral using the Riemann sum:
 
# ∫ab ​f(x)dx ≈ ∑f(xi​)Δx
# Δx = rectangle ki width
# # f(xᵢ) = rectangle ki height


import math

def integral(f, a, b, n=5000):
    delta_x = (b - a) / n
    total = 0
    for i in range(n):
        x_i = a + i * delta_x
        total += f(x_i) * delta_x
    return total

def inverse(x):
    return 1 / x

approx_value = integral(inverse, 1, 2, 5000)
exact_value = math.log(2)

print("Approximate integral:", approx_value)
print("Exact value ln(2):", exact_value)
