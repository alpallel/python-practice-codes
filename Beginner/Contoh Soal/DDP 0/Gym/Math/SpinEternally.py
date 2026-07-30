# Tulis solusi untuk Spin Eternally
import math

a = input()             # misal inputnya string "1 0" 
a_list = a.split(" ")   # ini dia misahin pake spasi dan jadi list [1, 0]
x = int(a_list[0])      # nilai x ada di list index 0 [*1*, 0] (index list mulai dari 0)
y = int(a_list[1])      # nilai y ada di list index 1 [1, *0*]

b = int(input())
b_rad = math.radians(b)

x_akhir = math.cos(b_rad) * x - math.sin(b_rad) * y
y_akhir = math.sin(b_rad) * x + math.cos(b_rad) * y

print(f"{x_akhir:.4f} {y_akhir:.4f}")   # print with format 4 angka dibelakang koma (tanpa pembulatan)

