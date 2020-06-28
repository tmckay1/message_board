from .MessageCharacters import MessageCharacters

class MessageCharactersTest(MessageCharacters):

    cA = [[0,1,1],[1,0,1],[0,1,1]]
    cB = [[1,1,1],[1,0,1],[0,1,0]]
    cC = [[0,1,1],[1,0,0],[0,1,0]]
    cD = [[1,1,1],[1,0,0],[0,1,1]]
    cE = [[1,1,1],[1,0,1],[1,0,1]]
    cF = [[1,1,1],[1,0,1],[1,0,1]]
    cG = [[0,1,1],[1,0,1],[1,0,1]]
    cH = [[1,1,1],[0,0,1],[1,1,1]]
    cI = [[1,0,0],[1,1,1],[1,0,0]]
    cJ = [[1,0,0],[1,1,1],[1,0,0]]
    cK = [[1,1,1],[0,0,1],[1,1,0]]
    cL = [[1,1,1],[0,0,0],[0,0,0]]
    cM = [[1,1,1],[0,1,0],[1,1,1]]
    cN = [[1,1,1],[0,1,0],[0,1,1]]
    cO = [[0,1,1],[1,0,0],[0,1,1]]
    cP = [[1,1,1],[1,0,1],[0,1,1]]
    cQ = [[0,1,1],[1,0,1],[1,1,1]]
    cR = [[1,1,1],[1,0,1],[0,1,0]]
    cS = [[0,1,1],[1,0,1],[1,0,1]]
    cT = [[1,0,0],[1,1,1],[1,0,0]]
    cU = [[1,1,1],[0,0,0],[1,1,1]]
    cV = [[1,1,1],[0,0,0],[1,1,1]]
    cW = [[1,1,1],[0,0,0],[1,1,1]]
    cX = [[1,1,0],[0,0,1],[1,1,0]]
    cY = [[1,1,0],[0,0,1],[1,1,0]]
    cZ = [[1,0,0],[1,0,1],[1,1,0]]

    c0 = [[1,1,1],[1,0,0],[1,1,1]]
    c1 = [[0,0,0],[1,1,1],[0,0,0]]
    c2 = [[1,0,1],[1,0,1],[1,1,1]]
    c3 = [[1,0,1],[1,0,1],[1,1,1]]
    c4 = [[1,1,1],[0,0,1],[1,1,1]]
    c5 = [[1,1,1],[1,0,1],[1,0,1]]
    c6 = [[1,1,1],[1,0,1],[1,0,1]]
    c7 = [[1,0,0],[1,0,0],[1,1,1]]
    c8 = [[1,1,1],[1,0,1],[1,1,1]]
    c9 = [[1,1,1],[1,0,1],[1,1,1]]

    cNULL          = [[0,0,0]]
    cSPACE         = [[0,0,0],[0,0,0],[0,0,0]]
    cPERIOD        = [[0,0,0],[0,0,0]]
    cCOMMA         = [[0,0,0],[0,0,0]]
    cDOUBLEQUOTE   = [[1,1,0],[1,1,0],[0,0,0]]
    cSINGLEQUOTE   = [[1,1,0],[0,0,0]]
    cCOMMA         = [[0,0,0],[0,0,0]]
    cEXCLAIMATION  = [[1,1,1],[0,0,0]]
    cQUESTION      = [[0,1,0],[1,0,0],[0,1,1],[0,0,0]]
    cUNKNOWN       = [[1,1,1],[1,1,1],[1,1,1]]