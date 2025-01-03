# 1. cara membuat string

data = "ini adalah string"
print(data)
print(type(data))

# 2. cara membuat string dengan single quote '...'
data = 'ini adalah string'
print(data)

# 3. menggunakan tanda \ pada string
# membuat tanda ' menjadi string
data = 'jum\'at'
print(data)

# 4. menggunakan tanda " pada string
data = "jum'at"
print(data)

# 5. backslash
# backlash \\
print("C:\\user\\Ucup")

# 6. tab \t
print("ucup\totong, jadi sahabat")

# 7. backspace \b
print("ucup \botong, jadi sahabat")

# 8. newline \n
print("baris pertama.\nbaris kedua.")

# 9. multiline string
print("""
ini adalah
multiline string
""")    # bisa juga menggunakan tanda '''...'''

# 10. string concatenation (concat)
nama_depan = "ucup"
nama_belakang = "otong"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

# 11. menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 12. operator untuk string
# mengambil karakter dari string
print(nama_lengkap[0])  # u
print(nama_lengkap[1])  # c
print(nama_lengkap[-1]) # g
print("nama = ",nama_lengkap[:4])  # ucup
print("nama = ",nama_lengkap[5:])  # otong
print("nama = ",nama_lengkap[0:4]) # ucup
print("nama = ",nama_lengkap[:])   # ucup otong

# raw string
print(r'halo\n')
print(r"""
      '\
      """)