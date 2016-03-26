# A* Shortest Path Algorithm
from heapq import heappush, heappop # for priority queue
import math
import time
import random
import sys

class Node:
    def __init__(self,value,pX,pY):
        self.value = value
        self.pX = pX
        self.pY = pY
        self.parent = None
        self.H = 0
        self.G = 0
    #if other is not obstacle, cost = 1
    def move_cost(self,other):
        cost = 0
        if self.value == 'X':
            cost = sys.maxsize
        elif self.value == '.':
            cost = 1
        return cost
        
               
def children(pX, pY,grid):
    x = pX
    y = pY
    points = []
    
    for p in [(x-1, y-1),(x,y - 1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y + 1),(x,y+1),(x+1,y+1)]:
        # print "Point",p
        if not (p[0] < 0 or p[0] >= len(grid) or p[1] < 0 or p[1] >= len(grid[0])):
            points.append(p)
    links = [grid[d[0]][d[1]] for d in points]
    links = [link for link in links if link.value =="."]
    print [(link.point, link.value) for link in links]
    return links

def manhattan(node1,node2):
    return abs(node1.pX - node2.pX) + abs(node1.pY-node2.pY)

#moving cost G value
def diagonal(node1, node2):
    dx = abs(node1.x - node2.x)
    dy = abs(node1.y - node2.y)
    #D is moving cost of moving - and ; D2 is moving cost of / and \
    D = 10
    D2 = 14
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
    
    
def aStar(start, goal, grid):
    #The open and closed sets
    openset = set()
    closedset = set()
    #Current point is the starting point
    current = start
    #Add the starting point to the open set
    openset.add(current)
    #While the open set is not empty
    while openset:
        #Find the item in the open set with the lowest G + H score
        current = min(openset, key=lambda o:o.G + o.H)
        #If it is the item we want, retrace the path and return it
        if current == goal:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]
        #Remove the item from the open set
        openset.remove(current)
        #Add it to the closed set
        closedset.add(current)
        #Loop through the node's children/siblings
        for node in children(current,grid):
            print node.point, node.value,current.move_cost(node)
            #If it is already in the closed set, skip it
            if node in closedset:
                continue
            #Otherwise if it is already in the open set
            if node in openset:
                #Check if we beat the G score 
                new_g = current.G + current.move_cost(node)
                if node.G > new_g:
                    #If so, update the node to have a new parent
                    node.G = new_g
                    node.parent = current
            else:
                #If it isn't in the open set, calculate the G and H score for the node
                node.G = current.G + current.move_cost(node)
                node.H = manhattan(node, goal)
                #Set the parent to our current item
                node.parent = current
                #Add it to the set
                openset.add(node)
    #Throw an exception if there is no path
    raise ValueError('No Path Found')
# def next_move(pacman,food,grid):
    #Convert all the points to instances of Node
         
###################################################
# A-star algorithm.
# Path returned will be a string of digits of directions.
def pathFind(the_map, directions, dx, dy, xStart, yStart, xFinish, yFinish):
    closed_nodes_map = [] # map of closed (tried-out) nodes
    open_nodes_map = [] # map of open (not-yet-tried) nodes
    dir_map = [] # map of directions
    row = [0] * n
    for i in range(m): # create 2d arrays
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

    pq = [[], []] # priority queues of open (not-yet-tried) nodes
    pqi = 0 # priority queue index
    # create the start node and push into list of open nodes
    n0 = node(xStart, yStart, 0, 0)
    n0.updatePriority(xFinish, yFinish)
    heappush(pq[pqi], n0)
    open_nodes_map[yStart][xStart] = n0.priority # mark it on the open nodes map

    # A* search
    while len(pq[pqi]) > 0:
        # get the current node w/ the highest priority
        # from the list of open nodes
        n1 = pq[pqi][0] # top node
        n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority)
        x = n0.xPos
        y = n0.yPos
        heappop(pq[pqi]) # remove the node from the open list
        open_nodes_map[y][x] = 0
        # mark it on the closed nodes map
        closed_nodes_map[y][x] = 1

        # quit searching when the goal state is reached
        # if n0.estimate(xFinish, yFinish) == 0:
        if x == xFinish and y == yFinish:
            # generate the path from finish to start
            # by following the directions
            path = ''
            while not (x == xStart and y == yStart):
                j = dir_map[y][x]
                c = str((j + directions / 2) % directions)
                path = c + path
                x += dx[j]
                y += dy[j]
            return path

        # generate moves (child nodes) in all possible directions
        for i in range(directions):
            xdx = x + dx[i]
            ydy = y + dy[i]
            if not (xdx < 0 or xdx > n-1 or ydy < 0 or ydy > m - 1
                    or the_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                # generate a child node
                m0 = node(xdx, ydy, n0.distance, n0.priority)
                m0.nextdistance(i)
                m0.updatePriority(xFinish, yFinish)
                # if it is not in the open list then add into that
                if open_nodes_map[ydy][xdx] == 0:
                    open_nodes_map[ydy][xdx] = m0.priority
                    heappush(pq[pqi], m0)
                    # mark its parent node direction
                    dir_map[ydy][xdx] = (i + directions / 2) % directions
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    # update the priority info
                    open_nodes_map[ydy][xdx] = m0.priority
                    # update the parent direction info
                    dir_map[ydy][xdx] = (i + directions / 2) % directions
                    # replace the node
                    # by emptying one pq to the other one
                    # except the node to be replaced will be ignored
                    # and the new node will be pushed in instead
                    while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    heappop(pq[pqi]) # remove the wanted node
                    # empty the larger size pq to the smaller one
                    if len(pq[pqi]) > len(pq[1 - pqi]):
                        pqi = 1 - pqi
                    while len(pq[pqi]) > 0:
                        heappush(pq[1-pqi], pq[pqi][0])
                        heappop(pq[pqi])       
                    pqi = 1 - pqi
                    heappush(pq[pqi], m0) # add the better node instead
    return '' # no route found

#convert file into map
def createMap(filename):
    f = open(filename,'r')
    li = [i.strip().split() for i in f.readlines()]
    return li
#convert map to map of nodes
def createGrid(map):
    grid = []
    for i in range(len(map)):
        row = map[i]
        for j in range(len(row)):
            col = row[j]
            node = Node(col, j, i)
            grid.append([node.pX,node.pY,node.value])
    return grid          
#find position of an element
def findPos(map,element):
    result = []
    for i in range(len(map)):
        row = map[i]
        for j in range(len(row)):
            col = row[j]
            if(col == element):
                result = [element, j, i]
    return result

# MAIN
directions = 8 # number of possible directions to move on the map
#manhattan distance
if directions == 4:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
elif directions == 8:
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

# map matrix

the_map = createMap('map.txt')
grid = createGrid(the_map)
print grid
#print the_map
n = len(the_map[0]) # horizontal size
m = len(the_map) # vertical size

print 'Map Size (X,Y): ', n, m
print 'Start: ', findPos(the_map, 'A')
print 'Finish1: ', findPos(the_map, 'B')
print 'Finish2: ', findPos(the_map, 'C')
t = time.time()
xA = findPos(the_map, 'A')[1]
yA = findPos(the_map, 'A')[2]
xB = findPos(the_map, 'B')[1]
yB = findPos(the_map, 'B')[2]
#xC = findPos(the_map, 'C')[1]
#yC = findPos(the_map, 'C')[2]

route = pathFind(the_map, directions, dx, dy, xA, yA, xB, yB)
print 'Time to generate the route (s): ', time.time() - t
print 'Route:'
print route

# mark the route on the map
if len(route) > 0:
    x = xA
    y = yA
    the_map[y][x] = 2
    for i in range(len(route)):
        j = int(route[i])
        x += dx[j]
        y += dy[j]
        the_map[y][x] = 3
    the_map[y][x] = 4

# display the map with the route
print 'Map:'
for y in range(m):
    for x in range(n):
        xy = the_map[y][x]
        if xy == '.':
            print '.', # space
        elif xy == 'X':
            print 'X', # obstacle
        elif xy == 'A':
            print 'S', # start
        elif xy == 3:
            print '@', # route
        elif xy == 4:
            print 'F', # finish
    print

raw_input('Press Enter...')