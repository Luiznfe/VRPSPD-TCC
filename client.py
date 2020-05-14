class Client:

    def __init__(self, id, dely, pick):
        self.id = id
        self.dely = dely
        self.pick = pick

    def getId(self):
        return self.id

    def getX(self):
        return self.coorX

    def getY(self):
        return self.coorY

    def getDely(self):
        return self.dely

    def getPick(self):
        return self.pick

    def setId(self, id):
        self.id = id

    def setX(self, x):
        self.coorX = x

    def setY(self, y):
        self.coorY = y

    def setDely(self,dely):
        self.dely = dely

    def setPick(self, pick):
        self.pick = pick

    def toString(self):
        return 'delivery : {} pick {}'.format(self.dely, self.pick)
