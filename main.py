'''Дана программа для Редактора:

НАЧАЛО
ПОКА нашлось (11)
    ЕСЛИ нашлось (112)
        ТО заменить (112, 6)
        ИНАЧЕ заменить (11, 3)
КОНЕЦ ПОКА
КОНЕЦ

Исходная строка содержит десять единиц и четыре двойки, других цифр нет, точный порядок расположения единиц и двоек 
неизвестен. Какую наибольшую сумму цифр может иметь строка, при том что сумма цифр будет простым числом?
'''
from random import *
from math import *

def prost(n):
    for i in range(2, int(sqrt(n))+1):           
        if n%i==0:
            return False
    return True

m = []
for _ in range (1000):
    f=10*"1"+4*"2"
    s=list(f)
    shuffle(s)
    s="".join(s)
    while "11" in s:
        if "112" in s :
            s = s.replace("112","6",1)
        else:
            s=s.replace("11","3",1)
    su=s.count("6")*6+s.count("2")*2+s.count("3")*3+s.count("1")*1
    if prost(su) == True:
        m.append(su)

print(max(m))
        
