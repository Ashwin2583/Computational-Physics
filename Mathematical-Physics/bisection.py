def func(x):
    f = x**3 - 2*x - 5
    return f

while True:
    a = int(input("Enter a: ")) 
    b = int(input("Enter b: "))
    if func(a)*func(b) > 0:
        continue
    else:
        break
j = 0
while True:
    c = (a + b)/2
    if abs(func(c))<0.000001:
        break
    if func(a) * func(c) < 0:
        b = c
    if func(c) * func(b) < 0:
        a = c
    j = j + 1

print("The loops executed",j,"times")
print("The value of root is ",c)