import Crypto.Util.number as cu

print("Write two non negative number: ")
a = int(input("Non negative number 1: "))
b = int(input("Non negative number 2: "))

while b > 0:
    r = a % b
    a = b
    b = r

    print(r)
