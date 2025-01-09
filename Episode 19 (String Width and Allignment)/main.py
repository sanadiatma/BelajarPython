# width and multiline

# data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string
data_string = f"nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Nomor Sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)

data_string = f"nama = {data_nama}, \nUmur = {data_umur}, \nTinggi = {data_tinggi}, \nNomor Sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String \\n"+5*"=")
print(data_string)

# string multiline (kutip triplets)

data_string = f"""Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
Nomor Sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"Data String kutip"+5*"=")
print(data_string)

# mengatur lebar


data_string = f"""
Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
Nomor Sepatu = {data_nomor_sepatu}

====================================
Nama         = {data_nama:>20}
Umur         = {data_umur:>20}
Tinggi       = {data_tinggi:>20}
Nomor Sepatu = {data_nomor_sepatu:>20}
"""

print("\n"+5*"="+"Data String pengaturan lebar"+5*"=")
print(data_string)