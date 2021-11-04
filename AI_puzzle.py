
# This will keep track of the nodes in graph search
class Node:
   def __init__(self, data=0, gValue=0, hValue=0, fValue=0):
      self.data = data

      self.parent = None

      self.direction = None

      self.gValue = 0
      self.hValue = 0
      self.fValue = 0

def individualH(elem, row, col, goalState):
    total = 0
    for line in goalState:
        if elem in line:
            goalRow = goalState.index(line)
            goalCol = line.index(elem)
            total = abs(goalRow - row) + abs(goalCol - col)
    return total
            

# Function to calulate f(n)
# Currenly only h(n)
def calcF(currState, goalState, wValue):
    hValue = 0
    for line in currState:
        for elem in line:
            hValue += individualH(elem, currState.index(line), line.index(elem), goalState)
    hValue *= wValue
    return int(hValue)

# create helper fucnction can if can move in each direction 

# create helper function to check if it is a repeated state 

def move(empty, state, rowLoc, colLoc, wValue, goalState):
    # Need to check if there is a tile in each direction around empty tile space
    up = rowLoc - 1
    down = rowLoc + 1
    left = colLoc + 1
    right = colLoc -1 

    # Check if there is a value to move for each direction then create a node 
    # Call function to calculate new f(n) for each node
    # Need to update state and keep count of nodes 
    if (0<up<len(state)):
        up = Node(state[up][colLoc])
    if (0<down<len(state)):
        down = Node(state[down][colLoc])
    if (0<left<len(state[0])):
        left = Node(state[left][rowLoc])
    if (0<right<len(state[0])):
        right = Node(state[right][rowLoc])



def main ():
    # open the file
    file = open("AI_puzzle_test.txt", "r")
    wValue = 1.0

    tempList = []
    state = []
    goalState = []
    index = 0
    breakAt = 0

    # Make a list
    for line in file:
        line = line.strip()
        line = line.split(' ')
        tempList.append(line)

    # current state
    state = tempList[0:3]

    # find initial position of empty tile
    for line in state:
        if '0' in line:
            colLoc = line.index('0')
            rowLoc = state.index(line)
    
    goalState = tempList[4:8]
    
    # maybe while loop
    # while state!=goalState:
    # add g counter in while loop
    empty = Node((state[rowLoc][colLoc]))
    theF = calcF(state, goalState, wValue)
    move(empty, state, rowLoc, colLoc, wValue, goalState)

    file.close()
main()
