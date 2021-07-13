import math

global intersection_dict, roads_list, pos_path, heuristic_values, next_cost
heuristic_values = {}
intersection_dict = {}
roads_list = []
pos_path = []

class  Priority_queue(object):
    def __init__(self):
        self.queue = []
        
    def __str__(self):
        return ' '.join([str(index) for index in self.queue])
    
    def isEmpty(self):
        return not self.queue
    
    def insert(self, data):
        self.queue.append(data)
        
    def delete(self):
        try:
            minimum = 0
            for index in range(len(self.queue)):
                if (self.queue[index][-1]+self.queue[index][-2]) < (self.queue[minimum][-1] + self.queue[minimum][-2]):
                    minimum = index
            item = self.queue[minimum]
            del self.queue[minimum]
            return item
        except IndexError:
            pass
            
def shortest_path(M, start, goal):
    if start == goal:
        return [start]
    global intersection_dict, roads_list, pos_path, heuristic_values, next_cost
    heuristic_values = {}
    intersection_dict = M.intersections
    roads_list = M.roads
    for node in intersection_dict:
        heuristic_values[node] = math.sqrt((intersection_dict[node][0] - intersection_dict[goal][0])**2 + abs(intersection_dict[node][1] - intersection_dict[goal][1])**2)
    next_cost = []
    for index in range(len(roads_list)):
        temp = []
        for path in roads_list[index]:
            temp.append(math.sqrt((intersection_dict[index][0] - intersection_dict[path][0])**2 + abs(intersection_dict[index][1] - intersection_dict[path][1])**2))
        next_cost.append(temp)
    print("shortest path called")
    pos_path = Priority_queue()
    pos_path.insert([[start],0,heuristic_values[start]])
    return helper_path(start, goal)

def helper_path(current, goal):
    global intersection_dict, roads_list, pos_path, heuristic_values, next_cost
    item = 0
    if pos_path.isEmpty():
        return "No possible path"
    else:
        item = pos_path.delete()
    current = item[0][-1]
    if current == goal:
        return item[0]
    for index,front in enumerate(roads_list[current]):
        if front in item[0]:
            continue
        g = next_cost[current][index] + item[-2]
        h = heuristic_values[front]
        pos_path.insert([item[0]+[front],g,h])
    return helper_path(current, goal)