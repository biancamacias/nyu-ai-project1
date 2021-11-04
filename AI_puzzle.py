# artificial intelligence project 1
# Isabel Huey, Bianca Macias
# ijh234, bm2815

# graph search will use this Node data structure throughout
class Node:
   def __init__(self, data = 0, g = 0, goal_state, weight):
      self.data = data # list, current state of puzzle
      self.parent = None # None if root, must be another node otherwise
      self.direction = None # TODO: maybe don't need this? we'll see

      self.g = g # node level
      self.h = self.calculate_h(goal_state) # Manhattan distances from goal state
      self.f = self.calculate_f(goal_state, weight) # f(n) = g(n) + h(n)

    def calculate_h(self, goal_state): # TODO: fix this
        # calculates manhattan distances of curr state from goal state
        total = 0
        for row in goal_state:
            if elem in line:
                goalRow = goal_state.index(row)
                goalCol = row.index(elem)
                total = abs(goalRow - row) + abs(goalCol - col)
        return total

    # Function to calulate f(n)
    # Currenly only h(n)
    def calculate_f(self, goal_state, weight): # TODO: fix this
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

    # puzzle list data structure: [[row 1], [row 2], [row 3]]
    initial_state = [] # initial state of puzzle
    state = []
    goal_state = [] # will hold goal state, input from input file
    index = 0
    states_created = [] # list to hold states already created
    breat_at = 0 # TODO: do we use this?

    # Make a list
    for line in file:
        line = line.strip()
        line = line.split(' ')
        initial_state.append(line)

    # current state
    curr_state = initial_state[0:3]

    # find initial position of empty tile
    for row in curr_state:
        if '0' in line:
            colLoc = row.index('0')
            rowLoc = curr_state.index(row)

    goal_state = initial_state[4:8]

    # maybe while loop
    # while state!=goalState:
    # add g counter in while loop
    # create root, then loop to create children
    root = Node(curr_state, 0) # TODO: data in node should be whole table
    f_value = calcF(curr_state, goal_state, w_value) # use g value
    move(empty, curr_state, rowLoc, colLoc, w_value, goal_state) # put this into a loop

    file.close()
main()
