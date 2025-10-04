print("=== Arithmetic Associate Law ===")
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

lhs_add = (a + b) + c
rhs_add = a + (b + c)

print(f"(a + b) + c = ({a} + {b}) + {c} = {lhs_add}")
print(f"a + (b + c) = {a} + ({b} + {c}) = {rhs_add}")

if lhs_add == rhs_add:
    print("Addition Associate Law holds")
else:
    print("Addition Associate Law does not holds")

lhs_mul = (a * b) * c
rhs_mul = a * (b * c)

print(f"(a * b) * c = ({a} * {b}) * {c} = {lhs_mul}")
print(f"a * (b * c) = {a} * ({b} * {c}) = {rhs_mul}")

if lhs_mul == rhs_mul:
    print("Multiplication Associate Law holds")
else:
    print("Multiplication Associate Law does not holds")

print("\n")

print("=== Boolean Associate Law ===")
print("Enter Boolean values as 1 (True) or 0 (False) : ")
A = bool(input("Enter value for A: "))
B = bool(input("Enter value for B: "))
C = bool(input("Enter value for C: "))

lhs_or = (A or B) or C
rhs_or = A or (B or C)

print(f"(A or B) or C = ({A} or {B}) or {C} = {lhs_or}")
print(f"A or (B or C) = {A} or ({B} or {C}) = {rhs_or}")

if lhs_or == rhs_or:
    print("OR Associate Law holds")
else:
    print("OR Associate Law does not holds")

lhs_and = (A and B) and C
rhs_and = A and (B and C)

print(f"(A and B) and C = ({a} and {b}) and {c} = {lhs_and}")
print(f"A and (B and C) = {a} and ({b} and {c}) = {rhs_and}")

if rhs_and == rhs_and:
    print("AND Associate Law holds")
else:
    print("AND Associate Law does not holds")