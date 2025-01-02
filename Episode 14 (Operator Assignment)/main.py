# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 9 # adalah assignment
b = 5
print("nilai a:", a)
print("nilai b:", b)

a += 1 # artinya a = a + 1
print("nilai a += 1, nilai a menjadi", a)

a-= 2 # artinya a = a - 2
print("nilai a -= 2, nilai a menjadi", a)

a *= 5 # artinya a = a * 5
print("nilai a *= 5, nilai a menjadi", a)

a /= 2 # artinya a = a / 2
print("nilai a /= 2, nilai a menjadi", a)

b = 5
b %= 2 # artinya a = b % 2
print("nilai b %= 2, nilai b menjadi", b)
b = 5
b **= 2 # artinya b = b ** 2
print("nilai b **= 2, nilai b menjadi", b)
b = 5
b //= 2 # artinya b = b // 2
print("nilai b //= 2, nilai b menjadi", b)

# operasi bitwise
c = True
print("\nnilai c:", c)
c &= False
print("nilai c &= False, nilai c menjadi", c)
c = True
c |= False
print("nilai c |= False, nilai c menjadi", c)
c = True
c ^= False
print("nilai c ^= False, nilai c menjadi", c)
c = True
