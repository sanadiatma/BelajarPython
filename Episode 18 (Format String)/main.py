# format string

# contoh generic
# string
nama = "marlene"
stir = "hello " + nama
print(stir)

format_str = f"hello {nama}"
print(format_str)

# angka
angka = 2005.5
stir = "angka = " + str(angka)
format_str = f"angka = {angka}"
print(stir)
print(format_str)

# boolean
boolean = True
stir = "boolean = " + str(boolean)
format_str = f"boolean = {boolean}"
print(stir)
print(format_str)

# bilangan ribuan
angka = 25000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"angka = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"angka = {angka:9.2f}"
print(format_str)
format_str = f"angka = {angka:09.2f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"minus = {angka_plus:+d}"
print(format_minus)
print(format_plus)

# memformat persen 
persentase = 0.035
format_persen = f"persen = {persentase}"
print(format_persen)
format_persen = f"persen = {persentase:%}"
print(format_persen)
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"harga total = Rp{harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 268
format_binary = f"binary = {str(bin(angka))}"
format_octal = f"octal = {str(oct(angka))}"
format_hex = f"hexadecimal = {str(hex(angka))}"

print(format_binary)
print(format_octal)
print(format_hex)