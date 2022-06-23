# Simple python code that first calls pow()
# then applies % operator.
a = int(input("Non negative number 1: "))
b = int(input("Non negative number 2: "))
pow = (int)(1e9 + 7)

# pow function used with %
d = pow(a, b) % pow
print(d)

