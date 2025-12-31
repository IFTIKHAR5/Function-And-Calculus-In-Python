# Implement a simple linear regression using gradient descent without any ML libraries: 
#  Define a loss function MSE = (1/n) * Σ(y_pred - y)^2. 
#  Compute derivatives w.r.t. slope m and intercept c. 
#  Update m and c using gradient descent. 
#  Test with a small dataset: x = [1,2,3,4], y = [2,4,6,8]. 

# Note to Students: 

#  Use only math library if necessary. 
#  Focus on functional programming—avoid classes, use pure functions. 
#  Test each function with different inputs. 
#  Compare numerical results with analytical solutions where possible


# ---------------------------------------------
# Simple Linear Regression using Gradient Descent
# No ML libraries, only pure Python
# ---------------------------------------------

# Step 1: Mean Squared Error (Loss Function)
# Yeh batata hai model kitna ghalat predict kar raha hai
def mse_loss(x, y, m, c):
    n = len(x)
    total_error = 0

    for i in range(n):
        # predicted value
        y_pred = m * x[i] + c

        # squared error
        total_error += (y_pred - y[i]) ** 2

    # average error
    return total_error / n


# Step 2: Gradients nikalna (derivatives w.r.t m and c)
# Gradient batata hai kis direction mein m aur c move karne hain
def gradients(x, y, m, c):
    n = len(x)
    dm = 0
    dc = 0

    for i in range(n):
        y_pred = m * x[i] + c
        error = y_pred - y[i]

        # derivative w.r.t m
        dm += error * x[i]

        # derivative w.r.t c
        dc += error

    dm = (2 / n) * dm
    dc = (2 / n) * dc

    return dm, dc


# Step 3: Gradient Descent algorithm
# Yeh m aur c ko bar-bar update karta hai
def gradient_descent(x, y, m, c, learning_rate=0.01, epochs=1000):
    for _ in range(epochs):
        dm, dc = gradients(x, y, m, c)

        # update rules
        m = m - learning_rate * dm
        c = c - learning_rate * dc

    return m, c


# Step 4: Dataset (Given in problem)
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# Step 5: Initial guess (start point)
m_initial = 0
c_initial = 0

# Step 6: Train model using Gradient Descent
m_final, c_final = gradient_descent(
    x, y, m_initial, c_initial,
    learning_rate=0.01,
    epochs=2000
)

# Step 7: Results
print("Learned slope (m):", m_final)
print("Learned intercept (c):", c_final)

# Step 8: Final loss
final_loss = mse_loss(x, y, m_final, c_final)
print("Final MSE Loss:", final_loss)
