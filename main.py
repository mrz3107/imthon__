#1
numbers = [5, 12, 3, 20, 7, 9]
data = (4, 7, 10, 3, 6, 1)

print("Eng katta:", max(numbers))
print("Eng kichik:", min(numbers))

juft_sonlar = []
for son in data:
    if son % 2 == 0:
        juft_sonlar.append(son)

print("Juft sonlar:", juft_sonlar)

#2
nums = [1, 2, 2, 3, 3, 3, 4]

unikal_sonlar = set(nums)

takrorlanish_soni = {}

for son in unikal_sonlar:
    takrorlanish_soni[son] = nums.count(son)

print(takrorlanish_soni)

#3
Baholar = {"Ali": 75, "Vali": 55, "Hasan": 90, "Olim": 40}

for ism in list(Baholar.keys()):
    if Baholar[ism] < 60:
        del Baholar[ism]

eng_yuqori = max(Baholar.values())

print(Baholar)
print("Eng yuqori baho:", eng_yuqori)

yigindi = 0

#5
from typing import List

def juft_sonlar_soni(sonlar: List[int]) -> int:
   
    count = 0
    for son in sonlar:
        if son % 2 == 0:
            count += 1
    return count

from typing import List

def juft_sonlar_soni(sonlar: List[int]) -> int:
   
    count = 0
    for son in sonlar:
        if son % 2 == 0:
            count += 1
    return count

sonlar = [1, 2, 3, 4, 5, 6, 7, 8]

print("Juft sonlar soni:", juft_sonlar_soni(sonlar))

#6
def ortacha(*args):
    if len(args) == 0:
        return 0  
    return sum(args) / len(args)

print(ortacha(10, 20, 30))
print(ortacha(5, 15)) 
print(ortacha())            

#7
import random

tasodifiy_son = random.randint(1, 100)

print("Tasodifiy son:", tasodifiy_son)

#8
try:
    with open("numbers.txt", "r") as f:
        numbers = [float(line) for line in f]

    average = sum(numbers) / len(numbers)
    print("O'rtacha qiymat:", average)

except:
    print("Xatolik yuz berdi!")

finally:
    print("Dastur tugadi.")