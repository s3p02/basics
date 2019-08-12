#RINGBUFFER
import logging
import sys

class ringBuffer:
    ring = []
    def __init__(self,bound):
        self.bound = bound
        logging.info("CLASS ringBuffer: bound initialized")
        logging.debug("CLASS ringBuffer: bound initialized")
    
    def appendBuff(self,element):
        logging.info("CLASS ringBuffer: appendBuff METHOD")
        if len(self.ring) >= self.bound:
            self.ring.pop(0)
            logging.debug("CLASS ringBuffer: appendBuff METHOD: popped ring[0]")
        self.ring.append(element)
        logging.debug("CLASS ringBuffer: appendBuff METHOD: appended "+str(element))
    def full(self,buff):
        logging.info("CLASS ringBuffer: appendBuff METHOD")
        if len(buff) > self.bound:
            ibuff = buff[-self.bound:]
            logging.debug("CLASS ringBuffer: full METHOD: ring[-bound:]")
            self.ring = ibuff
            logging.debug("CLASS ringBuffer: full METHOD: ring = ibuff ")
        else:
            self.ring = buff