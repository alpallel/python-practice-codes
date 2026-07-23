# DONE: import library yang diperlukan
import math

print("=" * 60)
print("SELAMAT DATANG DI SISTEM PENCATATAN PENDUDUK FLORIAN!")
print("=" * 60)

print("\n==== Data Penduduk ====")

# DONE: lengkapi input-input di bawah ini
nama = input("Nama : ")
tempat_lahir = input("Tempat Lahir : ")
tanggal_lahir = input("Tanggal Lahir : ")
spesies = input("Spesies : ")
tinggi = float(input("Tinggi (dalam m) : "))
berat = float(input("Berat (dalam kg) : "))

# DONE: hitung tinggi dan luas rumah
# refer kembali ke rumus yang disediakan pada soal
tinggi_rumah = tinggi + 0.85
luas_rumah = (math.pi * math.sqrt(2) * (tinggi ** 2)) + (berat/3)

# DONE: tampilkan luaran sesuai dengan test case yang ada pada dokumen soal
# ingat bahwa bilangan dibulatkan dua angka di belakang koma
print("==== Ringkasan Data Penduduk ====")
print(f"Penduduk berspesies {spesies} dengan nama {nama} yang lahir tanggal {tanggal_lahir} di {tempat_lahir} berhasil terdaftar menjadi penduduk negeri Florian!")
print()
print(f"{nama} berhak atas rumah dengan tinggi {round(tinggi_rumah,2)} meter dan luas {round(luas_rumah,2)} meter persegi.")

print()

print("=" * 60)
print("TERIMA KASIH SUDAH MELAKUKAN PENCATATAN DATA PENDUDUK!")
print("=" * 60)