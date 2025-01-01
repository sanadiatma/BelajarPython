# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka
def benarsalah (b):
    if b is True:
        return "benar"
    elif b is False:
        return "salah"
    


# +++++3-----10+++++
inputuser = float(input("masukan angka yang bernilai \nkurang dari 3\natau\nlebih besar dari 10\n:"))



# +++++3----------
# memeriksa angka kurang dari 3
kurangdari = (inputuser < 3)
if kurangdari == True:
    print(f"{inputuser} kurang dari 3")
else:
    print(f"{inputuser} lebih dari 3")

# ----------10+++++   
# memeriksa angka lebih dari 10
lebihdari = (inputuser > 10)
if lebihdari == True:
    print(f"{inputuser} lebih dari 10")
else:
    print(f"{inputuser} kurang dari 10")


#jawaban anda
print("JAWABAN ANDA")
jawaban1 = kurangdari or lebihdari
print(benarsalah(jawaban1),"\n")
    
print(20*"-")
    
# -----3+++++10-----
inputuser = float(input("\nmasukan angka yang bernilai \nlebih besar dari 3\ndan\nkurang dari 10\n:"))



# -----3++++++++++
# memeriksa angka kurang dari 3
lebihdari = (inputuser > 3)
if lebihdari == False:
    print(f"{inputuser} kurang dari 3")
else:
    print(f"{inputuser} lebih dari 3")

# +++++10----------  
# memeriksa angka lebih dari 10
kurangdari = (inputuser < 10)
if kurangdari == False:
    print(f"{inputuser} lebih dari 10")
else:
    print(f"{inputuser} kurang dari 10")


#jawaban anda
print("JAWABAN ANDA")
jawaban2 = kurangdari and lebihdari
print(benarsalah(jawaban2))