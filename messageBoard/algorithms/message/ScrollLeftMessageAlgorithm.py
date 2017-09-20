from .MessageAlgorithm import MessageAlgorithm

class ScrollLeftMessageAlgorithm(MessageAlgorithm):

    def __init__(self):
        super(ScrollLeftMessageAlgorithm, self).__init__()

    def animateLED(self,led, step, word, cAlgorithm):

        width    = led.width
        height   = led.height
        xStart   = width - step
        ledRange = step 

        for xShift in range(ledRange):
            for y in range(height):
                x = xStart + xShift
                if x > 0:
                    if xShift < len(word):
                        if word[xShift][y]:
                            color = cAlgorithm.getColor(led,xShift,y,step)
                            led.set(x,y,color)
                        else:
                            led.set(x,y,(0,0,0))
                    else:
                        led.set(x,y,(0,0,0))

        #if we've reached the end of the word, just exit for now
        if step >= len(word) + led.width:
            print('done')
            exit(0)
