'''Для какого наибольшего целого неотрицательного числа А выражение

(x + 3y > A)V(x < 30)V(y < 30)

тождественно истинно?'''
def f(a12):
    for x in range (-100,100):
        for y in range (-100,100):
            if ((x+3*y>a12) or (x<30)or(y<30))==0:
                return 0
    return 1
for a12 in range (-100,1000):
    if f(a12)==1:
        print (a12)
        