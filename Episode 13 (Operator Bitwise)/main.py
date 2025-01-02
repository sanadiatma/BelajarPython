# operator bitwise adalah operator yang digunakan untuk melakukan operasi pada bit/biner

a = 9
b = 5

# bitwise OR
c = a | b
print("\n========== OR ==========")
print("nilai a:", a, "binary:", format(a, '08b'))
print("nilai b:", b, "binary:", format(b, '08b'))
print("------------------------ (|)")
print("hasil :", c, "binary:", format(c, '08b'))

#bitwise AND
c = a & b
print("\n========== AND ==========")
print("nilai a:", a, "binary:", format(a, '08b'))
print("nilai b:", b, "binary:", format(b, '08b'))
print("------------------------ (&)")
print("hasil :", c, "binary:", format(c, '08b'))

#bitwise XOR
c = a ^ b
print("\n========== XOR ==========")
print("nilai a:", a, "binary:", format(a, '08b'))
print("nilai b:", b, "binary:", format(b, '08b'))
print("------------------------ (^)")
print("hasil :", c, "binary:", format(c, '08b'))

#bitwise NOT
c = ~a
print("\n========== NOT ==========")
print("nilai a:", a, "binary:", format(a, '08b'))
print("------------------------ (~)")
print("hasil :", c, "binary:", format(c, '08b'))

#shift right
c = a >> 1
print("\n========== SHIFT RIGHT ==========")
print("nilai a:", a, "binary:", format(a, '08b'))
print("------------------------ (>>)")
print("hasil :", c, "binary:", format(c, '08b'))

#shift left
c = a << 1
print("\n========== SHIFT LEFT ==========")
print("nilai a:", a, "binary:", format(a, '08b'))
print("------------------------ (<<)")
print("hasil :", c, "binary:", format(c, '08b'))
