A,B,H,M = map(int, input().split())

#Ｈ時0分のとき、30*Ｈ°の開き。
#1分ごとに、この差は5.5*Ｍごと縮まるので、
#abs(30*H-5.5M)°の開きが出る
import math
C=math.sqrt(A**2+B**2-2*A*B*math.cos(abs(30*H-5.5*M)*math.pi/180))
print("{:.15f}".format(C))
