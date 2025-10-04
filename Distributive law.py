print("Arithmetic Distributive Law")
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

lhs = a * (b * c)
rhs = (a * b) + (a * c)

print(f"LHS = {a} * ({b} * {c}) = {lhs}")
print(f"RHS = ({a} * {b}) + ({a} * {c}) = {rhs}")

if lhs == rhs:
    print("Distributive Law holds for arithmetic!\n")
else:
    print("Not Equal")

print("--------------------------")
print(" Boolean Distributive Law ")
print("Enter Boolean values as 1 (True) or 0 (False) : ")
A = bool(int(input("Enter value for A: ")))  
B = bool(int(input("Enter value for B: ")))
C = bool(int(input("Enter value for C: ")))

lhs_bool = a and (b or c)
rhs_bool = (a and b) or (a and c)

print(f"LHS = {A} and ({B} or {C}) = {lhs_bool}")
print(f"RHS = ({A} and {B}) or ({A} and {C}) = {rhs_bool}")

if lhs_bool == rhs_bool:
    print("Distributive Law holds for Boolean logic!\n")
else:
    print("Not Equal")