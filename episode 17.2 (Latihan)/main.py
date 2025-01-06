#aplikasi pengecek judul

print("silahkan masukan judul dan kami akan mengeceknya")

data1 = input("silahkan masukan judul\n:")

cek_judul = data1.istitle()
if cek_judul == True:
    print(f"{data1} merupakan judul")
else:
    print(f"{data1} bukanlah judul")
    