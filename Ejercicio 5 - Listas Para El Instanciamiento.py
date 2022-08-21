from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
puerto=[23,22,21,19,18,05,26,27,04,02,15]
t=[]

for i in puerto:
    t.append (pin(i,pin.OUT))
print(t)
def derecha():
    for i in t:
        for j in range(9):
            i.value(not i.value())
        pausam(100)
def izquierda():
    for i in reversed(t):
        for j in range(9):
            i.value(not i.value())
        pausam(100)
while True:
    derecha()
    izquierda()