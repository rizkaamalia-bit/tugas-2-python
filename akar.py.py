#Program menghitung akar suatu bilangan
#Nama programmer = Rizka Amalia
#Tanggal = 07 Febuari 2025

import math

# Meminta input dari pengguna
angka = float(input("Masukkan angka untuk dihitung akarnya: "))

# Angka negatif tidak dapat diakarkan
if angka < 0:
    print("Eror")
else:
    akar: float = math.sqrt(angka) #Rumus menghitung akar
    print(f"Akar dari {angka} adalah {akar}")


