class Solution:

    def __init__(self):
        self.id = id
        self.vehicleList = list()
        self.clientList = list()
        self.adjMatix = list()
        self.capacity = 0

    def setId(self, id):
    	self.id = id

    def set_vehicleList(self, vehicle):
    	self.vehicleList = vehicle.copy()

    def set_clientList(self, client):
    	self.clientList = client.copy() 

    def setCapacity(self, cap):
        self.capacity = cap

    def set_adjMatrix(self, matrix):
    	self.adjMatix = matrix.copy()

    def get_vehicleList(self):
    	return self.vehicleList

    def getId(self):
    	return self.id

    def get_clientList(self):
    	return self.clientList

    def get_adjMatrix(self):
    	return self.adjMatix

    def getCapacity(self):
    	return self.capacity

