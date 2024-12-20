'''Черепахе был дан для исполнения следующий алгоритм:

Повтори 9 [Вперёд 22 Направо 90 Вперёд 6 Направо 90]
Поднять хвост
Вперёд 1 Направо 90 Вперёд 5 Налево 90
Опустить хвост
Повтори 9 [Вперёд 53 Направо 90 Вперёд 75 Направо 90].

Определите периметр области объединения фигур, 
ограниченных заданными алгоритмом линиями.'''
from turtle import*
k=5
tracer(0)
for _ in range (9):
    forward(22*k)
    right(90)
    forward(6*k)
    right(90)
pu()
forward(1*k)
right(90)
forward(5*k)
left(90)
pd()
for _ in range (9):
    forward(53*k)
    right(90)
    forward(75*k)
    right(90)
pu()
for x in range (-50,50):
    for y in range (-50,100):
        setpos(x*k,y*k)
        dot(3,"green")
done()


