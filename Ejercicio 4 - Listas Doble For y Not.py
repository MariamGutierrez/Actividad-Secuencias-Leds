from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
leda=pin(23,pin.OUT)
ledb=pin(22,pin.OUT)
ledc=pin(21,pin.OUT)
ledd=pin(19,pin.OUT)
lede=pin(18,pin.OUT)
ledf=pin(05,pin.OUT)
ledg=pin(26,pin.OUT)
ledh=pin(27,pin.OUT)
ledi=pin(04,pin.OUT)
ledj=pin(02,pin.OUT)
ledk=pin(15,pin.OUT)
ledt=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh,ledi,ledj,ledk]
def derecha():
    for i in ledt:
        for j in range (2):
            i.value(not i.value())
            pausam(5)
def izquierda():
    for i in reversed(ledt):
        for j in range(2):
            i.value(not i.value())
            pausam(5)
while True:
    derecha()
    izquierda()