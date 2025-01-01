# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is.is not

a = 4
b = 2

# lebih besar dari >
print(10*"=","lebih besar dari",10*"=")
hasil = a > 3
print(f"a > 3 = {hasil}")
print(20*"-")
hasil = b > 3
print(f"b > 3 = {hasil}")
print(20*"-")
hasil = b > 2
print(f"b > 2 = {hasil}")

# kurang dari <
print(10*"=","kurang dari",10*"=")
hasil = a < 3
print(f"a < 3 = {hasil}")
print(20*"-")
hasil = b < 3
print(f"b < 3 = {hasil}")
print(20*"-")
hasil = b < 2
print(f"b < 2 = {hasil}")

# lebih besar sama dengan >=
print(10*"=","lebih besar sama dengan",10*"=")
hasil = a >= 3
print(f"a >= 3 = {hasil}")
print(20*"-")
hasil = b >= 3
print(f"b >= 3 = {hasil}")
print(20*"-")
hasil = b >= 2
print(f"b >= 2 = {hasil}")

# kurang dari sama dengan >=
print(10*"=","kurang dari sama dengan",10*"=")
hasil = a <= 3
print(f"a <= 3 = {hasil}")
print(20*"-")
hasil = b <= 3
print(f"b <= 3 = {hasil}")
print(20*"-")
hasil = b <= 2
print(f"b <= 2 = {hasil}")

# sama dengan ==
print(10*"=","sama dengan",10*"=")
hasil = a == 4
print(f"a == 4 = {hasil}")
print(20*"-")
hasil = b == 3
print(f"b == 3 = {hasil}")

# tidak sama dengan ==
print(10*"=","tidak sama dengan",10*"=")
hasil = a != 4
print(f"a != 4 = {hasil}")
print(20*"-")
hasil = a != 3
print(f"a != 3 = {hasil}")

# is sebagai komparasi object identity
print(10*"=","is",10*"=")
x = 5
y = 5
z = 6
hasil = x is y
print(f"x is y = {hasil}")
hasil = x is z
print(f"x is z = {hasil}")

# is not sebagai komparasi object identity
print(10*"=","is",10*"=")
x = 5
y = 5
z = 6
hasil = x is not y
print(f"x is not y = {hasil}")
hasil = x is not z
print(f"x is not z = {hasil}")