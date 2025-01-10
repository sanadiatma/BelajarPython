# Date and Time

import datetime

# menghitung umur

hari_ini = datetime.date.today()
print(f"{hari_ini:%A}")

tanggal = datetime.date(1999,6,10)
print(tanggal)

print("Silahkan masukan tanggal, bulan dan tahun lahir")
tanggal = int(input("Tanggal\t\t:"))
bulan = int(input("Bulan\t\t:"))
tahun = int(input("Tahun\t\t:"))

tanggal_lahir = datetime.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari nya adalah           : {tanggal_lahir:%A}")
umur = hari_ini-tanggal_lahir
print(f"Umur anda adalah: {umur}")