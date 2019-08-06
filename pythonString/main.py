import logging
import sys
from pythonString import *


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    st1 = myString("Customers")
    logging.debug("RESULT:"+st1.getReverse())
    name1 = "Customers"
    name2 = "Store SCUM"
    myAnagrams(name1,name2).check()
    myAnagrams("funeral","real fun").check()