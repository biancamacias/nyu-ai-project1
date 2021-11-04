
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
    w_value = 1.0 # TODO: change this

    initial_state = []
    state = []
    goal_state = []
    index = 0
    breat_at = 0

    # Make a list
    for line in file:
        line = line.strip()
        line = line.split(' ')
        initial_state.append(line)

    # current state
    curr_state = initial_state[0:3]

    # find initial position of empty tile
    for line in curr_state:
        if '0' in line:
            colLoc = line.index('0')
            rowLoc = state.index(line)

    goal_state = initial_state[4:8]

    # maybe while loop
    # while state!=goalState:
    # add g counter in while loop
    empty = Node((curr_state[rowLoc][colLoc]))
    f_value = calcF(curr_state, goal_state, w_value)
    move(empty, curr_state, rowLoc, colLoc, w_value, goal_state)

    file.close()
main()
