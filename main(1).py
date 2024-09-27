'''При каком наибольшем целом A найдутся такие целые неотрицательные x и y, что выражение
(3x+y>48)V(x>y)V(4x+y<A)
будет ложным?'''
def f(a):
    for x in range (0,100):
        for y in range(0,100):
            if(( 3*x + y >48) or (x>y) or (4*x+y<a))==0:
                return 0
    return 1
for a in range(1,1000):
    if f(a)==0:
        print(a)   
            
 

