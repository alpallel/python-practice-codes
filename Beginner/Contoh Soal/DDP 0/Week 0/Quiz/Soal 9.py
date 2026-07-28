import math

# TODO: Input
waktu = int(input())
pusat_x = int(input())
pusat_y = int(input())
jari_jari = int(input())
sudut_awal = int(input())

# TODO: Hitung sudut
sudut_akhir = sudut_awal + (6 * waktu)
sudut_radian = ((sudut_akhir / 180) % 360) * math.pi

# TODO: Hitung koordinat akhir
x_akhir = jari_jari * math.cos(sudut_radian) + pusat_x
y_akhir = jari_jari * math.sin(sudut_radian) + pusat_y

# Output
print(f"Koordinat titik akhir: ({x_akhir:.2f}, {y_akhir:.2f})")