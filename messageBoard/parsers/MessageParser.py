

class MessageParser(object):

	_message     = ""
	_messageList = []
	_characters  = None

	def __init__(self, message, characters):
		super(MessageParser, self).__init__()
		self._message    = message.upper()
		self._characters = characters
		self.setMessage(self._message)

	def setMessage(self,message):
		#reset message list
		self._messageList = []

		#calculate message list
		for letter in message:
			binaryLetter = self.getBinaryLetter(letter)
			self._messageList.extend(binaryLetter)
			self._messageList.extend(self._characters.cNULL)

		#set our new message
		self._message = message

	def getMessage(self):
		return self._message

	def getMessageList(self):
		return self._messageList

	def printMessage(self):
		for y in range(len(self._messageList[0])):
			for x in range(len(self._messageList)):
				if self._messageList[x][y]:
					print(0)
				else:
					print(" ")
			print("")

	def getBinaryLetter(self,letter):

		binaryLetter = self._characters.cUNKNOWN

		#if we have the letter defined add it to the list, otherwise check for special character
		if hasattr(self._characters,"c"+letter):
			binaryLetter = self._characters.__getattribute__("c"+letter)
		elif letter == " ":
			binaryLetter = self._characters.cSPACE
		elif letter == ".":
			binaryLetter = self._characters.cPERIOD
		elif letter == ",":
			binaryLetter = self._characters.cCOMMA
		elif letter == "!":
			binaryLetter = self._characters.cEXCLAIMATION
		elif letter == "?":
			binaryLetter = self._characters.cQUESTION
		elif letter == "\"":
			binaryLetter = self._characters.cDOUBLEQUOTE
		elif letter == "'":
			binaryLetter = self._characters.cSINGLEQUOTE

		return binaryLetter












		
