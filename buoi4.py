# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:37:56 2024

@author: Tran Thi Tuyet Mai
Bài 1: khoảng cách độ dài đến trường
distance = float(input("Nhập độ dài đến trường (m):"))
if distance <300:
    print("Đường đến trường quá gần. Thôi! Đi bộ.")
elif distance > 1200: 
    print("Đường đến trường quá xa. Thôi! Đi xe máy.")
elif distance >= 300 and distance <= 700:
    print("Đường đến trường không xa. Thôi! Đi xe đạp.")
else:
    print("Không xác định")

bài 2: gpa
gpa = float(input("Nhập điểm trung bình (GPA):"))
if gpa <3.5:
    print("Học lực kém")
elif gpa <= 3.5 and gpa < 5.0:
    print("Học lực yếu")
elif gpa <= 5.0 and gpa < 7.0:
    print("Học lực trung bình")
elif gpa <= 7.0 and gpa < 8.0:
    print("Học lực khá")
elif gpa <= 8.0 and gpa < 9.0:
    print("Học lực giỏi")

else:
    print("Học lực xuất sắc")
    
Bài 3:Phương trình bậc 1
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trinh vô nghiệm")
elif a != 0  and b == 0:
    print("Phương trình có nghiệm a==0")
elif a != 0 and b!= 0:
    print("Phương trình có nghiệm x=", -b/a)
    
bài 4: Phương trình bậc 2
import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số b: "))
denta = b*b - 4*a*c
if a == 0: 
    print("phương trình có nghiệm duy nhất x=", -b/c)
elif a != 0 and denta < 0:
    print("phương trình vô nghiệm")
elif a != 0 and denta == 0:
    print("phương trình có nghiệm kép x1=x2 = ", -b/(2*a))
elif a != 0 and b*b - (4*a*c) > 0:
    print("Phuong trinh có 2 nghiệm pb x1 = ", (-b + math.sprt(denta))/(2*a))
    print("phương trình có 2 nghiệm pb x2 = ", (-b - math.sprt(denta))/(2*a))

bài 5: tam giác đặc biệt
a = float(input("nhập a= "))
b = float(input("nhập b= "))
c = float(input("nhập c= "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("đây là tam giác đều")
    elif a*a + b*b + c*c:
        print("đây là tam giác vuông ")
    elif a == b and b == c and c == a:
        print("đây là tam giác cân")
    else:
        print("đây là tam giác")
        
else:
    print("đây không phải là tam giác")
    
bài 6:  chứng minh tam giác 
a = float(input("nhập a= "))
b = float(input("nhập b= "))
c = float(input("nhập c= "))
if a + b > c and a + c > b and b + c > a:
    print(" đây là tam giác")
else:
    print("đây không phải là tam giác")

    
bài 7: kéo búa bao
import random
choices = [" kéo", " búa" , "bao"]
kq_nguoi_choi= input("Nhập kết quả người chơi")
if kq_nguoi_choi not in [" kéo", "búa", "bao"]:
    print("không hợp lệ vui lòng nhập lại")
kq_may= random.choice(choices)
print("kq may", kq_may)
if kq_nguoi_choi == kq_may:
    print("kq hòa")
elif (kq_nguoi_choi == "kéo" and kq_may == "bao") or\
     (kq_nguoi_choi == "búa" and kq_may == "kéo") or\
     (kq_nguoi_choi == "bao" and kq_may == "búa"):
         print("bạn thắng")
else:
     print("bạn thua")

bài 8: tính quãng đường
d = float(input("nhập quãng đường đã đi (km)"))
if d <=1:
    print("giá là 20K")
elif d > 1 and d <= 4: 
    print("giá là:", d*13000)
elif d >= 4 and d <= 8:
    print("giá là:", (3*13000)+ (d-3)*12000)
else: 
    print("giá là:", 39000 + 60000 + (d-8)*10000)
    m= 39000 + 60000 + (d-8)*10000
    if m >= 100000:
        print("giá là sau khi giảm:", m*0.92)
    


"""



