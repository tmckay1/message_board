from bibliopixel.layout import *
from bibliopixel.drivers.PiWS281X import *
from bibliopixel.layout import Rotation
from messageBoard.animations.MessageBoardAnimation import MessageBoardAnimation
from messageBoard.parsers.MessageParser import MessageParser
from messageBoard.characters.MessageCharacters5x3 import MessageCharacters5x3
from messageBoard.algorithms.message.ScrollLeftMessageAlgorithm import ScrollLeftMessageAlgorithm
from messageBoard.algorithms.color.RainbowColorAlgorithm import RainbowColorAlgorithm
import time
import sys

#get message
if(len(sys.argv) !=2):
    print("Only insert 1 command line argument that is the message to display")
    exit(1)
message = sys.argv[1]

#create biblio pixel driver and led
vert_flip  = False   # flip across x-axis
serpentine = False   # serpentine pattern
thread     = False   # display updates to run in background thread
coordMap   = None    # coordinate mapping array
width      = 47      # width of board
height     = 5       # height of board
brightness = 100     # brightness 0-255
driver     = PiWS281X(47*5)
led        = Matrix(driver, width, height, coordMap, Rotation.ROTATE_0, vert_flip, serpentine, thread, brightness)

#create binary word to display from character set
characters = MessageCharacters5x3()
parser     = MessageParser(message, characters)
binaryWord = parser.getMessageList()
#parser.printMessage()

#run animation
delay      = .15 
mAlgorithm = ScrollLeftMessageAlgorithm()
cAlgorithm = RainbowColorAlgorithm()
anim       = MessageBoardAnimation(led,binaryWord,mAlgorithm,cAlgorithm,delay)
anim.run()
