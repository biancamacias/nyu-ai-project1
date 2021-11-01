
# This will keep track of the nodes in graph search
class Node:
   def __init__(self, data=0, gValue=0, hValue=0, fValue=0):
      self.data = data

      self.left = None
      self.right = None
      self.up = None
      self.down = None

      self.direction = None

      self.gValue = 0
      self.hValue = 0
      self.fValue = 0

# Function to calulate f(n)
def calcF(state, goalState, wValue):
    None
    # Code to calulate f(n)



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
        empty.up = up 
    if (0<down<len(state)):
        down = Node(state[down][colLoc])
        empty.down = down 
    if (0<left<len(state[0])):
        left = Node(state[left][rowLoc])
        empty.left = left 
    if (0<right<len(state[0])):
        right = Node(state[right][rowLoc])
        empty.right = right

    
    

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
    empty = Node((state[rowLoc][colLoc]))
    move(Node, state, rowLoc, colLoc, wValue, goalState)


    
    file.close()
main()