# artificial intelligence project 1
# Isabel Huey, Bianca Macias
# ijh234, bm2815

WEIGHTS = [1, 1.2, 1.4]

# graph search will use this Node data structure throughout
class Node:
   def __init__(self, state = 0, g = 0, goal_state, weight):
      self.state = state # list, current state of puzzle
      self.parent = None # None if root, must be another node otherwise
      self.direction = None # TODO: maybe don't need this? we'll see

      self.g = g # node level
      self.h = self.calculate_h(goal_state) # Manhattan distances from goal state
      self.f = self.calculate_f(weight) # f(n) = weight * h(n) + g(n)

    def calculate_h(self, goal_state):
        # calculates manhattan distances of curr state from goal state
        total = 0
        for goal_row in range(0,3):
            for goal_column in range(0,4):
                goal_element = goal_state[goal_row][goal_column]
                curr_row, curr_column = find_element(goal_element)
                total += abs(goal_row - curr_row) + abs(goal_column - curr_column)
        return total

    def find_element(self, element):
        # finds row, column of element in the current state
        # returns tuple of its location (row, column)
        for row in range(0, 4):
            for column in range(0,5):
                if self.state[row][column] == element:
                    return row, column

    def calculate_f(self, weight):
        # calculates f value
        return weight * self.h + self.g

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



def main():
    # open the file
    file = open("AI_puzzle_test.txt", "r")
    weight = 1.0 # TODO: change this

    # puzzle list data structure: [[row 1], [row 2], [row 3]]
    initial_state = [] # initial state of puzzle
    state = []
    goal_state = [] # will hold goal state, input from input file
    index = 0
    states_created = [] # list to hold states already created
    breat_at = 0 # TODO: do we use this?
    g = 0 # g(n) value, root starts at

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
    # check if initial state == goal state, then loop
    # add g counter in while loop
    # create root, then loop to create children
    root = Node(curr_state, 0, goal_state, weight) # TODO: data in node should be whole table
    move(empty, curr_state, rowLoc, colLoc, weight, goal_state) # put this into a loop

    file.close()

if __name__ == '__main__':
    main()
