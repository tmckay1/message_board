from bibliopixel.layout import *
from bibliopixel.animation import BaseMatrixAnim
from bibliopixel.drivers.PiWS281X import *
from bibliopixel.layout import Rotation
import time

class MessageBoardAnimation(BaseMatrixAnim):

    _word       = [] 
    _delay      = 0.0
    _mAlgorithm = None
    _cAlgorithm = None

    def __init__(self, led, word, mAlgorithm, cAlgorithm, delay = 0.2):
        #The base class MUST be initialized by calling super like this
        super(BaseMatrixAnim, self).__init__(led)
        self._word       = word
        self._mAlgorithm = mAlgorithm
        self._cAlgorithm = cAlgorithm
        self._delay      = delay

    # override to write out word for each frame in the animation
    def step(self, amt = 1):
        self._mAlgorithm.animateLED(self._led, self._step, self._word, self._cAlgorithm)
        self._step += amt
        time.sleep(self._delay)











