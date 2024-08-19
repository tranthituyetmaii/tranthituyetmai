# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:29:29 2024

@author: Trần Thị Tuyết Mai
Bài 1:Trung bình cộng
a = int(input("nhap a "))
b = int(input("nhap b "))
c = int(input("nhap c:"))
d = int(input("nhap d:"))
trung_binh = (a + b + c + d )/4
print("tong trung a,b,c,d la:", trung_binh)

Bài 2: 2 số nguyên a,b
a = int(input("nhap a:"))
b = int(input("nhap b:"))
tong = (a + b)
hieu = (a - b)
tich = (a * b)
thuong = round ((a / b), 2)
chia_lay_phan_du = (a % b)
chia_lay_phan_nguyen = (a // b)
print(" a + b =", tong)
print(" a - b =", hieu)
print(" a * b =", tich)
print(" a / b =", thuong)
print("a / b = ", round(a / b, 3))
print(" a % b=", chia_lay_phan_du)
print(" a // b=", chia_lay_phan_nguyen)

Bài 3: Tổng 2 số nguyên dương
n = int(input("nhap so nguyen duong co 2 chu so"))
chu_so_hang_chuc = n // 10
chu_so_hang_don_vi = n % 10
tong_cac_chu_so = chu_so_hang_chuc + chu_so_hang_don_vi  
if 10 <= n <= 99:
  print("tong cac chu so cua n", tong_cac_chu_so) 
  
Bài 4: Giờ, phút, giây
cách 1:
thoi_gian = input ("nhap thoi gian (hh:mm:ss):")
gio, phut, giay = map(int, thoi_gian.split(":"))
tong_giay = gio *3600 + phut *60 + giay
print(" tong so giay la:", tong_giay)
cách 2:
gio = int(input("nhap gio"))
phut = int(input("nhap phut"))
giay = int(input("nhap giay"))
tong_giay = gio *3600 + phut *60 + giay
print("tong so giay la", tong_giay)

Bài 5: Năm sinh
nam_sinh = int(input("nhap năm sinh"))
nam_hien_tai = 2024
tuoi = nam_hien_tai - nam_sinh
print("so tuoi la", tuoi)

Bài 6: phương trình bậc 2
a = float(input("nhập a"))
b = float(input("nhập b"))
c = float(input("nhập c"))
print(f" { a }X^2 +  { b }X + {c}  = 0")

Bài 7: menu
print("========MENU=======")
print(" 1. Hu tieu ")
print(" 2. Chao long ")
print(" 3. Banh canh ")
print(" 4. Bun rieu ")
print(" 5. Pho bo ")
print("==================")
input(" Moi nhap lua chon ")
print("==================")
print(" sự lựa chọn của bạn là:")

Bài 8: phép tính mũ
A = (32 ** 0.2) - ((1/64) ** -0.25) + ((8/27) ** (1/3))
a = round(A, 3)
print(" kết quả là", a)

Bài 9: phương trình căn bậc
import math
a = int(input("nhập số a"))
b = int(input("nhập số b"))
A = (math.sqrt(a) - math.sqrt(b)) / ((a ** (1/4)) - (b ** (1/4)))
B = (math.sqrt(a) + ((a * b) ** (1/4))) / ((a ** (1/4)) + (b ** (1/4)))
print("kết quả của phép tính là:", A - B)




    
"""


