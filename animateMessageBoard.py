from bibliopixel.layout import Matrix
from bibliopixel.layout.geometry import Rotation
from messageBoard.animations.MessageBoardAnimation      import MessageBoardAnimation # import the animation
from messageBoard.characters.MessageCharacters5x3       import MessageCharacters5x3  # import the character set
from messageBoard.algorithms.RainbowColorAlgorithm      import RainbowColorAlgorithm # import color algorithm
from messageBoard.algorithms.ScrollLeftMessageAlgorithm import ScrollLeftMessageAlgorithm # import message algorithm
from messageBoard.parsers.StandardMessageParser         import StandardMessageParser # import the parser
from bibliopixel.drivers.PiWS281X import *
import sys

#get message from command line
if(len(sys.argv) !=2):
    print("Only insert 1 command line argument that is the message to display")
    exit(1)
message = sys.argv[1]

#create biblio pixel driver and led
vert_flip  = False   # flip across x-axis
y_flip     = False   # flip across y-axis
serpentine = True    # serpentine pattern
thread     = False   # display updates to run in background thread
width      = 58      # width of board
height     = 5       # height of board
brightness = 100     # brightness 0-255
driver     = PiWS281X(height*width)
led        = Matrix(driver, width, height, Rotation.ROTATE_0, vert_flip, y_flip, serpentine, thread, brightness)

# get word
characterSet  = MessageCharacters5x3()
messageParser = StandardMessageParser(message,characterSet)
word          = messageParser.getMessageMatrix()

# get algorithms
colorAlgorithm   = RainbowColorAlgorithm()
messageAlgorithm = ScrollLeftMessageAlgorithm(colorAlgorithm)

#run animation
delay = .15 
anim  = MessageBoardAnimation(led,word,messageAlgorithm,delay)
anim.run()

