class Vehicle:

    def __init__(self, num , cap ):
        self.num = num
        self.cap = cap
        self.route = list()
        self.dis = 0

    def getNum(self):
        return self.num

    def getCap(self):
        return self.cap

    def getRoute(self):
        return self.route

    def getDistance(self):
        return self.dist

    def setNum(self, num ):
        self.num = num

    def setCap(self, cap ):
        self.cap = cap

    def setRoute(self, route):
        self.route = route[:]

    def setDistance(self, dis):
        self.dis = dis

    def toString(self):
        return 'num : {} dis : {} cap : {} '.format(self.num, self.dis, self.cap)
