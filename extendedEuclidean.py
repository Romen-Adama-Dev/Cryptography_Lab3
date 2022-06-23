import Crypto.Util.number as cu

def extended_euclidean(a, b):
  if b == 0:
    gcd, s, t = a, 1, 0
    return (gcd, s, t)
  else:
    s2, t2, s1, t1 = 1, 0, 0, 1
    while b > 0:
      q= a // b
      r, s, t = (a - b * q), (s2 - q * s1), (t2 - q * t1)
      a, b, s2, t2, s1, t1 = b, r, s1, t1, s, t
    gcd, s, t = a, s2, t2
    return (gcd,s,t)

print("Write two non negative number: ")
a = int(input("Non negative number 1: "))
b = int(input("Non negative number 2: "))
r = extended_euclidean(a, b)

print(f"GCD({a},{b})={r[0]}")
print(f"Linear combination gcd(a,b)=sa+tb:\n {r[0]}={r[1]}*{a}+{r[2]}*{b}")