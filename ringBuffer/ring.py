#RINGBUFFER
import logging
import sys

class ringBuffer:
    ring = []
    avg = 0.0
    acount = 0
    def __init__(self,bound):
        self.bound = bound
        logging.info("CLASS ringBuffer: bound initialized")
        logging.debug("CLASS ringBuffer: bound initialized")
    
    def average(self):
        if self.acount > 0:
            logging.info("CLASS ringBuffer: average METHOD RE-COMPUTE")
            sumRing = sum(self.ring)
            self.avg = float(sumRing)/float(self.bound)
            self.acount = 0
            return self.avg 
        else:
            logging.info("CLASS ringBuffer: average METHOD CACHE")
            return self.avg
    
    def erase(self):
        logging.info("CLASS ringBuffer: clear METHOD")
        del self.ring[:]
        logging.info("CLASS ringBuffer: clear METHOD: cleared ring")
        self.acount +=1

    
    def get(self):
        logging.info("CLASS ringBuffer: get METHOD")
        return self.ring
    
    def appendBuff(self,element):
        logging.info("CLASS ringBuffer: appendBuff METHOD")
        if len(self.ring) >= self.bound:
            self.ring.pop(0)
            logging.debug("CLASS ringBuffer: appendBuff METHOD: popped ring[0]")
        self.ring.append(element)
        logging.debug("CLASS ringBuffer: appendBuff METHOD: appended "+str(element))
        self.acount +=1
    
    def full(self,buff):
        logging.info("CLASS ringBuffer: appendBuff METHOD")
        logging.debug("CLASS ringBuffer: full METHOD: buff = "+str(buff))
        buffLen = len(buff)
        if buffLen > self.bound:
            logging.debug("CLASS ringBuffer: full METHOD: buffLen > bound ----- "+str(buffLen)+" > "+str(self.bound))
            ibuff = buff[-self.bound:]
            logging.debug("CLASS ringBuffer: full METHOD: ibuff = buff[-"+str(self.bound)+":] ----- "+str(ibuff))
            self.ring = ibuff
            logging.debug("CLASS ringBuffer: full METHOD: ring = "+str(self.ring))
            self.acount +=1
        else:
            self.ring = buff