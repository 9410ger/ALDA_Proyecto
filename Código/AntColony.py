import numpy as np
import time
from numpy.random import choice as np_choice

class AntColony(object):

    def __init__(self, distances, time_windows, service_times, n_ants, n_iterations, decay, alpha, slack, best_enable,time_break):
        
        self.distances  = distances
        self.time_windows = time_windows
        self.service_times = service_times
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.slack = slack
        self.best_enable = best_enable
        self.start_time = time.time()
        self.time_break = time_break
            
    def run(self):
        distance_logs=[]
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        i = 0
        while(i < self.n_iterations and time.time() < self.start_time + self.time_break):
            all_paths = self.gen_all_paths()
            if(len(all_paths) != 0):
                self.spread_pheronome(all_paths, shortest_path=shortest_path)
                shortest_path = min(all_paths, key=lambda x: x[1])
                if shortest_path[1] < all_time_shortest_path[1]:
                    all_time_shortest_path = shortest_path
                distance_logs.append(all_time_shortest_path[1])
            i+=1
        return all_time_shortest_path,distance_logs
    
    def spread_pheronome(self, all_paths, shortest_path):
        for i in range(len(self.pheromone)):
            for j in range(len(self.pheromone)):
                if(i != j):
                    self.pheromone[i][j] += (1.0 - self.decay)* self.pheromone[i][j]
        for path, dist in all_paths[:self.n_ants]:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    def reduce_pheromone(self,impossible_path):
        self.pheromone[impossible_path[-2]] += ((self.decay - 1.0)* self.pheromone[impossible_path[-2]])
                 
    def gen_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele]
        return total_dist
    
    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            if(path != None):
                all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        impossible_path = False
        ant_time = 0
        path = []
        visited = set()
        visited.add(start)
        prev = start
        try:
            for i in range(len(self.distances) - 1):
                if(not impossible_path):
                    move,ant_time,impossible_path = self.pick_move(self.pheromone[prev], self.distances[prev], visited, ant_time,impossible_path)
                    path.append((prev, move))
                    prev = move
                    visited.add(move)
                else:
                    raise Exception()
            path.append((prev, start))  
            return path
        except:
            self.reduce_pheromone(path)
            pass
    
    def pick_move(self, pheromone, dist, visited, ant_time,impossible_path):
        move = None
        try:
            node_probability = 0.0
            row = np.array([])
            pheromoneTemp = np.copy(pheromone)
            pheromoneTemp[list(visited)] = 0
            for i in range(len(pheromoneTemp)):
                if(pheromoneTemp[i] != 0.0):
                    if(ant_time + dist[i] > self.time_windows[i][1]):
                        move = i
                        raise Exception
            for i in range(len(pheromoneTemp)):
                pheromone_probability = (pheromoneTemp[i] ** self.alpha)
                slack_time = self.time_windows[i][1] - (ant_time + dist[i])
                best_enable_time = self.time_windows[i][0] - (ant_time + dist[i])
                if(slack_time == 0):
                    slack_time = 0.0000001
                if(best_enable_time <= 0):
                    best_enable_time = 0.0000001
                slack_probability = (1.0 / abs(slack_time))** self.slack
                best_enable_time_probability = (1.0 / abs(best_enable_time)) ** self.best_enable
                node_probability = pheromone_probability * slack_probability * best_enable_time_probability
                row = np.append(row,node_probability)
                node_probability = 0.0
            norm_row = np.array([])
            row_sum = row.sum()
            for i in range(len(row)):
                if(row[i] == 0):
                    norm_row = np.append(norm_row,0)
                else:
                    norm_row = np.append(norm_row,row[i]/row_sum)
            move = np_choice(self.all_inds, 1, p=norm_row)[0]
            ant_time += dist[move]
            if (ant_time < self.time_windows[move][0]):
                ant_time = self.time_windows[move][0]
            return move,ant_time,impossible_path
        except:
            impossible_path = True
            return move,ant_time,impossible_path


        
