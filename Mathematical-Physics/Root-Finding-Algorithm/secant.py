tol = 0.001

# The function is defined here
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

x0 = float(input("Enter the first value: "))
x1 = float(input("Enter the second value: "))

while abs(x1 - x0) > tol:
    x2 = x1 - (f(x1)*(x1 - x0)) / (f(x1) - f(x0))
    x0, x1 = x1, x2


print("The root of the equation is ", x1)