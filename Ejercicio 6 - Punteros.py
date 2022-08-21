from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
p=[23,22,21,19,18,05,26,27,04,02,15]
t=[]

for i in p:
    t.append (pin(i,pin.OUT))
print(t)
inicio=0
fin=11
def derecha(op, end):
    for i in t[op:end]:
        for j in range(11):
            i.value(not i.value())
    pausam(160)
def izquierda(op, end):
    for i in reversed(t[op:end]):
        for j in range(11):
            i.value(not i.value())
        pausam(160)
while True:
    derecha(inicio, fin)
    izquierda(inicio, fin)