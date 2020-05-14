from client import Client
from solution import Solution

def data_entry():

    data = list()
    f = open("C:/Users/luizn/Desktop/ProjetoTCC/c0530.txt", "r")
    if f.mode == 'r':
        data = f.readlines()

    cap = float(data[0])
    n = b = int(data[1]) + 1
    linha = list()
    adjMatix = list()
    del data[0]
    del data[0]
    for i in range(0, n):
        for j in range(0, b):
            linha.append(float(data[j]))        
        adjMatix.append(linha[:])
        linha.clear()
        for j in range(0, b):
            data.pop(0)

    clientList = list()
    i = 0
    for k in range(0, len(data), 2):
        c = Client(i, data[k], data[k+1])
        clientList.append(c)

    s = Solution()
    s.setCapacity(cap)
    s.set_adjMatrix(adjMatix)
    s.


data_entry()
