from bibliopixel.layout import *
from bibliopixel.animation import BaseMatrixAnim
import time

class MessageBoardAnimation(BaseMatrixAnim):

    _word       = []
    _mAlgorithm = None
    _delay      = 0.2

    def __init__(self, led, word, mAlgorithm, delay):
        #The base class MUST be initialized by calling super like this
        super(BaseMatrixAnim, self).__init__(led)
        self._word       = word 
        self._mAlgorithm = mAlgorithm 
        self._delay      = delay

    # override to write out word for each frame in the animation
    def step(self, amt = 1):
        self._mAlgorithm.animateLED(self._led, self._step, self._word)
        self._step += amt
        time.sleep(self._delay)
