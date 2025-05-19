'''
Сколько существует десятичных четырёхзначных чисел, в которых все цифры различны и никакие две чётные или две
нечётные цифры не стоят рядом?
x = '1221'
'''

from itertools import *

chet = '02468'
nchet = '13579'
c = 0
for x in product('0123456789', repeat=4):       # x = ['1', '4', '3']
    x = ''.join(x)
    if x[0] != '0' and len(set(x)) == 4:
        x = x.replace('0', '2').replace('4', '2').replace('6', '2').replace('8', '2')
        x = x.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        if '22' not in x and '11' not in x:
            c += 1
            
print(c)