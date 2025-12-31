# Challenge 5: 
# Modify the bell curve to f(x) = exp(-(x-1)^2) and compute the area from 0 to 2. Relate 
# to probability. 

# Objective: 
# Approximate the probability under a normal-like curve using integration.



import math

# Step 1: Integral function (Riemann Sum)
def integral(f, a, b, n=2000):
    delta_x = (b - a) / n
    total = 0
    for i in range(n):
        x_i = a + i * delta_x
        total += f(x_i) * delta_x
    return total

#Define a simple bell-shaped function 
def bell_curve(x):
    return math.exp(-x**2)

# Approximate area under curve from 0 to 2 
area = integral(bell_curve, 0, 2, n=2000)
print("Area under bell curve from 0 to 2:", area)

# Normalize to approximate probability (approx. 95% for true normal)
print("Approx. probability between 0 and 2:", area / math.sqrt(math.pi))
