'''Для какого наименьшего целого неотрицательного числа А выражение

(x < A)V(y > A)V(y < x - 1)V(y < 2x - 3)

тождественно истинна, то есть принимает значение 1 при любых целых неотрицательных x и y?
'''

def f(A):
    for x in range(101):    
        for y in range(101):
            if ((x < A)or(y > A)or(y < x - 1)or(y < 2*x - 3))==0:
                return 0
    return 1
for A in range(101):
    if f(A)==1:
        print(A)
        break
            