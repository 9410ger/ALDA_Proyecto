import numpy as np
from sys import stdin
import sys
from AntColony import AntColony

def main():
    file_name = sys.argv[1]
    time_break = int(sys.argv[2])
    file = open(file_name,"r")
    nodos = int(file.readline())
    matriz = [None for x in range(nodos)]
    servicios = []
    timeWindows = [None for x in range(nodos)]
    for i in range(nodos):
        matriz[i] = list(map(float,file.readline().strip().split()))
    for i in range(nodos):
        timeWindows[i] = list(map(float,file.readline().strip().split()))
    matriz = np.array(matriz)
    timeWindows = np.array(timeWindows)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                servicios.append(matriz[i][j])
                matriz[i][j] = np.inf
                    
    servicios = np.array(servicios)
    ant_colony = AntColony(matriz,timeWindows,servicios,500,250,0.7,2,3,2,time_break)
    shortest_path,log = ant_colony.run()
    print ("shortest_path: {}".format(shortest_path))
    file.close()
main()
