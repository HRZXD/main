import statistics
import os

list= []
while True:
    Number = int(input("ใส่ตัวเลขในนี้ : "))
    if Number > 0:
        list.append(Number)
    elif Number <0:
        break

def mx(o):
    max = o[0]
    for x in o:
        if x > max :
            max = x
    return max

maxs = list
mx1 = (mx(maxs))

def mn(p):
    min = p[0]
    for y in p:
        if y < min :
            min = y
    return min

mins = list
mn1 = (mn(mins))

average = statistics.mean(list)
os.system('cls')

print("List ของตัวเลขที่ป้อน : " , list)
print("ค่าสูงสุดของ List : ", mx1)
print("ค่าต่ำสุดของ List : ", mn1)
print("ค่าเฉลี่ยของList นี้ : ", average)

