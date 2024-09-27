'''При каком наибольшем целом A найдутся такие целые неотрицательные x и y, что выражение

(x + 2y > 48)V(y > x)V(x + 3y < A)

будет ложным?

'''

def f(a):                           
    for x in range(1, 100):         
        for y in range(1, 100):     
            if ( (x + 2*y > 48) or (y > x) or (x + 3*y < a))   == 0:
                return 0
    return 1

for a in range(1, 1000):
    if f(a) == 0:
        print(a)
