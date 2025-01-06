# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case

salam = "halo halo !"
print("normal :"+salam)
print("upper :"+salam.upper())

# merubah semua ke lower

alay = "AkOe KeccE AbiEEzzZZz"
print("normal :"+alay)
print("lower :"+alay.lower())

## pengecekan dengan isX method

# contoh pengecekan dengan lower case

salam = "sist"
apakah_lower = salam.islower()
print(f"apakah {salam} adalah lower = {str(apakah_lower)}")

# contoh pengecekan dengan lower case
apakah_upper = salam.isupper()
print(f"apakah {salam} adalah upper = {str(apakah_upper)}")

# contoh pengecekan title
judul = "It Is Okay Not To Be Orkay"
apakah_judul = judul.istitle()
print(f"Apakah {judul} merupakan tittle = {str(apakah_judul)}")

# contoh penggunaan startwith dan endwith

cek_start = "halo apa kabar".startswith("halo")
print(f"apakah halo apa kabar dimulai dengan halo = {cek_start}")

cek_end = "halo apa kabar".endswith("kabar")
print(f"apakah halo apa kabar diakhiri dengan kabar = {cek_end}")

pisah = ['aku','adalah','aku']
gabung = ' '.join(pisah)
print(pisah)
print(gabung)

gabung = "aku77adalah77aku"
pisah  = gabung.split('77')
print(gabung)
print(pisah)

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(20)
print("|"+kanan+"|")

kiri = "kiri".ljust(20)
print("|"+kiri+"|")

tengah = "tengah".center(20)
print("|"+tengah+"|")

tengah = "tengah".center(20,":")
print("|"+tengah+"|")

tengah = tengah.strip(":")
print(tengah)