# operasi dan manipulasi string

# 1. menyambung string (concatenate)

nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "surucup"

nama_lengkap = nama_pertama + nama_tengah + nama_akhir
print(nama_lengkap)

nama_lengkap = nama_pertama +" "+ nama_tengah +"'"+ nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_pertama)
print("Panjang",nama_pertama,":",panjang)

panjang = len(nama_tengah)
print("Panjang",nama_tengah,":",panjang)

panjang = len(nama_akhir)
print("Panjang",nama_akhir,":",panjang)

panjang = len(nama_lengkap)
print("Panjang",nama_lengkap,":",panjang)

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string

status = "p" in nama_lengkap
print(status)

# mengulang string
print(10*"ha","wk"*10)

#indexing
print("index ke 5 dari "+ nama_lengkap +" adalah: "+nama_lengkap[5])
print("index ke -5 dari "+ nama_lengkap +" adalah: "+nama_lengkap[-5])
print("index ke [0:3] dari "+ nama_lengkap +" adalah: "+nama_lengkap[0:4])
print("index ke [0,2,4,6,8,10] dari "+ nama_lengkap +" adalah: "+nama_lengkap[0:10:2])

# item paling kecil
print(min(nama_lengkap))
# item paling besar
print(max(nama_lengkap))


ascii_code = ord(" ")
print(f"ASCII untuk ' ' adalah {ascii_code}")
ascii_code = ord("u")
print(f"ASCII untuk 'u' adalah {ascii_code}")

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print(f"Jumlah 'o' di nama {data} adalah {jumlah}")