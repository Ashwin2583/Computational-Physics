import cmath

a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c
d = cmath.sqrt(b**2 - 4*a*c)

# Calculate the two solutions
root1 = (-b + d) / (2 * a)
root2 = (-b - d) / (2 * a)

if discriminant > 0:
    print("The roots are real and distinct. And the roots are", root1, root2)
elif discriminant < 0:
    print("The roots are complex conjugates. And the roots are", root1, root2)
elif discriminant == 0:
    print("The roots are real and equal. And the roots are", root1, root2)


