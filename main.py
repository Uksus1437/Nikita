'''Рассмотрим шестнадцатеричные четырёхзначные числа. Сколько существует таких чисел, y которых:

1. B записи числа присутствует две чётные и две нечётные цифры.
2. Сумма чётных цифр равна сумме нечётных цифр.
3. Ни одна из цифр не повторяется.


f = '278A'

{2, 7, 8, A}
'''
ch_alph = '02468ACE'
nch_alph = '13579BDF'
c=0
v=0
for i1 in "123456789ABCDEF":
    for i2 in "0123456789ABCDEF":
        for i3 in "0123456789ABCDEF":
            for i4 in "0123456789ABCDEF":
                d=i1+i2+i3+i4
                ch = [i for i in d if i in ch_alph] 
                nch = [i for i in d if i in nch_alph]
                if len(ch)==2:
                    sm_ch = int(ch[0],16) + int(ch[1],16)
                    sm_nch = int(nch[0],16)+int(nch[1],16)
                    if sm_ch==sm_nch:
                        if len(set(d))==4:
                            c+=1
print(c)



