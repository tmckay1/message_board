from .ColorAlgorithm import ColorAlgorithm
import bibliopixel.colors as colors

class RainbowColorAlgorithm(ColorAlgorithm):

    def __init__(self):
        super(RainbowColorAlgorithm, self).__init__()

    def getColor(self,led,x,y,step):

        #    modifiedValue = (step + x) % 255
        modifiedValue = (step) % 255
        color = colors.hue2rgb(modifiedValue)
            
        return color
