# operasi logika atau boolean

# not, or, and, xor

print("=====NOT=====")
a = True
c = not a
print(f"data a = {a}")
print("-----------NOT")
print(f"data c = {c}")

print("=====OR=====")
a = False
b = False
c = a or b
print(f"{a} OR {b} = {c}")

a = False
b = True
c = a or b
print(f"{a} OR {b} = {c}")

a = True
b = False
c = a or b
print(f"{a} OR {b} = {c}")

a = True
b = True
c = a or b
print(f"{a} OR {b} = {c}")

print("=====AND=====")
a = False
b = False
c = a and b
print(f"{a} AND {b} = {c}")

a = False
b = True
c = a and b
print(f"{a} AND {b} = {c}")

a = True
b = False
c = a and b
print(f"{a} AND {b} = {c}")

a = True
b = True
c = a and b
print(f"{a} AND {b} = {c}")

print("=====XOR=====")
a = False
b = False
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = False
b = True
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = True
b = False
c = a ^ b
print(f"{a} XOR {b} = {c}")

a = True
b = True
c = a ^ b
print(f"{a} XOR {b} = {c}")