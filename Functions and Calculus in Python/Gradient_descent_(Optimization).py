# Challenge 4: 
# Use gradient descent to minimize f(x) = x^4 - 5x^2 + 6 starting from x=2. Try different 
# learning rates.

# Objective: 
# Implement a simple gradient descent to find the minimum of a function.



# Derivative function (limit definition)
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

#  Define gradient descent function
def gradient_descent(f, initial_x, learning_rate=0.02, epochs=100):
    x = initial_x
    for _ in range(epochs):

        grad = derivative(f, x)
        x = x - learning_rate * grad
    return x

# Define a convex function: f(x) = (x^4 - 5x^2 + 6)
def convex(x):
    return (x ** 4 - 5 * x ** 2 + 6)

#  Find minimum starting from x=2

min_x = gradient_descent(convex, initial_x=2)
print("minimum found at x =", min_x)
print("minimum value f(x) =", convex(min_x))
