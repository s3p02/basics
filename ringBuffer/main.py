#MAIN
from ring import *
import logging

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    d = ringBuffer(6)
    d.full([1,2,3,4,5,6,7,8,9,10])
    d.appendBuff(11)
    print(d.get())
    d1 = ringBuffer(5)
    d1.appendBuff(12)
    d1.appendBuff(13)
    d1.appendBuff(14)
    d1.appendBuff(15)
    d1.appendBuff(16)
    d1.appendBuff(17)
    print(d1.get())
    d1.erase()
    print(d1.get())
    d1.appendBuff(18)
    d1.appendBuff(19)
    d1.appendBuff(20)
    print(d1.average())
    print(d1.average())
    d1.appendBuff(21)
    d1.appendBuff(22)
    print(d1.get())
    print(d1.average())
    print(d1.average())