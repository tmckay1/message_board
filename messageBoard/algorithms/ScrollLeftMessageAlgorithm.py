from .MessageAlgorithm import MessageAlgorithm

class ScrollLeftMessageAlgorithm(MessageAlgorithm):

    def __init__(self, colorAlgorithm):
        super(ScrollLeftMessageAlgorithm, self).__init__(colorAlgorithm)

    # override to perform word animation
    def animateLED(self,led, step, word):

        # define variables
        boardWidth   = led.width
        maxStep      = boardWidth + len(word) # letter is off the board at this step
        xRange       = boardWidth
        yRange       = led.height
        xWordOffset  = step - boardWidth 

        # loop through range of x values in board
        for xBoard in range(xRange):
            # create mapping to x value of word
            xWord  = xWordOffset + xBoard
            for y in range(yRange):
                # only continue if the x coordinate of the word exists otherwise draw the empty color to the board
                color = self._colorAlgorithm.getEmptyColor(led,xBoard,y,step)
                if xWord >= 0 and xWord < len(word):
                    if word[xWord][y]:
                        color = self._colorAlgorithm.getColor(led,xBoard,y,step)
                led.set(xBoard,y,color)

        if step >= maxStep: # end animation when the letter is off the board
            exit(0)
