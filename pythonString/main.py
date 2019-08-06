import logging
import sys
from pythonString import *


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    st1 = myString("Sree")
    logging.debug("RESULT:"+st1.getReverse())