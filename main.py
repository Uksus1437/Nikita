'''Текстовый файл состоит из символов A, B и C.
Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.
Для выполнения этого задания следует написать программу.

BCBCAACB
B*CAA*
'''
f=open('24.txt').readline()
f=f.replace("AB", "*").replace("CB", "*")
co=0
mx = 0
for i in range(len(f)):
    if f[i]=="*":
        co+=1
        mx=max(mx, co)
    else:
        co=0
print(mx)
    
    
       
          