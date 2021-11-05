# artificial intelligence project 1
# Isabel Huey, Bianca Macias
# ijh234, bm2815

WEIGHTS = [1.0, 1.2, 1.4]
DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

# graph search will use this Node data structure throughout
class Node:
   def __init__(self, state = 0, g = 0, goal_state, weight):
      self.state = state # list, current state of puzzle
      self.parent = None # None if root, must be another node otherwise

      self.g = g # node level
      self.h = 0 # manhattan distances from goal state, will be 0 when goal is reached
      self.f = 0 # f(n) = weight * h(n) + g(n)

      self.calculate_h(goal_state)
      self.calculate_f(weight)

    def calculate_h(self, goal_state):
        # calculates manhattan distances of curr state from goal state
        # sets h value
        total = 0
        for goal_row in range(0,3):
            for goal_column in range(0,4):
                goal_element = goal_state[goal_row][goal_column]
                curr_row, curr_column = find_element(goal_element)
                total += abs(goal_row - curr_row) + abs(goal_column - curr_column)
        self.h = total

    def calculate_f(self, weight):
        # calculates and sets f value
        self.f = weight * self.h + self.g

    def find_element(self, element):
        # finds row, column of element in the current state
        # returns tuple of its location (row, column)
        for row in range(0, 4):
            for column in range(0,5):
                if self.state[row][column] == element:
                    return row, column

    def find_empty_tile(self):
        # TODO: create helper function to find empty tile position
        # returns tuple (row, column)

    def move_possible(self, direction):
        # TODO: create helper fucnction can if can move in each direction
        # takes direction (from DIRECTIONS list)
        # returns True or False if tile can move in that direction

def best_node(child_nodes):
    # TODO: create helper function to decide which child node is best based on f value
    # returns tuple (direction, node with lowest f value)

def move_up(node, g):
    # TODO: helper function that takes current node and creates new node where tile moves up
    # returns new node with node as its parent

def move_down(node, g):
    # TODO: helper function that takes current node and creates new node where tile moves down
    # returns new node with node as its parent

def move_left(node, g):
    # TODO: helper function that takes current node and creates new node where tile moves left
    # returns new node with node as its parent

def move_right(node, g):
    # TODO: helper function that takes current node and creates new node where tile moves right
    # returns new node with node as its parent

def generate_children(node, generated_states):
    # helper function that generates valid children based on directions they can move in
    # if new child state has already been generated before, skip it (no repeated states allowed)
    # if not, add to generated_states and children list
    # returns children list
    # value of children will be None if direction is not allowed
    new_up = None
    new_down = None
    new_left = None
    new_right = None
    if node.move_possible(DIRECTIONS[0]):
        new_up = move_up(node, g)
        if new_up.state not in generated_states:
            generated_states.append(new_up.state)
        else:
            new_up = None
    if node.move_possible(DIRECTIONS[1]):
        new_down = move_down(node, g)
        if new_down.state not in generated_states:
            generated_states.append(new_down.state)
        else:
            new_down = None
    if node.move_possible(DIRECTIONS[2]):
        new_left = move_left(node, g)
        if new_left.state not in generated_states:
            generated_states.append(new_left.state)
        else:
            new_left = None
    if node.move_possible(DIRECTIONS[3]):
        new_right = move_right(node, g)
        if new_right.state not in generated_states:
            generated_states.append(new_right.state)
        else:
            new_right = None
    return [new_up, new_down, new_left, new_right]

def move(node, g, generated_states):
    # creates nodes if empty tile can move up, down, left, right
    # and if the node has not yet been created
    # sets child node parent to node
    # returns tuple (direction taken, node with best f acc to A* search)

    child_nodes = generate_children(node, generated_states)
    # [up node or None, down node or None, left node or None, right node or None]

    return best_node(child_nodes)

def main():
    # open the file
    file = open("AI_puzzle_test.txt", "r")
    weight = WEIGHTS[1] # TODO: change this

    # puzzle state data structure: [[row 1], [row 2], [row 3]]
    initial_state = [] # initial state of puzzle
    goal_state = [] # will hold goal state, input from input file
    generated_states = [] # list to hold states already created to prevent repeated states
    g = 0 # g(n) value, root starts at 0
    optimal_path = [] # list of directions taken

    # Make a list
    for line in file:
        line = line.strip()
        line = line.split(' ')
        initial_state.append(line)

    # current state
    curr_state = initial_state[0:3]

    # find initial position of empty tile
    # for row in curr_state:
    #     if '0' in line:
    #         colLoc = row.index('0')
    #         rowLoc = curr_state.index(row)

    goal_state = initial_state[4:8]

    # create root, then start generating graph tree
    root = Node(curr_state, 0, goal_state, weight)
    generated_states.append(root.state)
    goal_reached = False
    curr_best_node = root
    while !(goal_reached):
        g += 1
        if curr_best_node.state == goal_state:
            goal_reached = True
        else:
            direction, next_node = move(curr_best_node, g, generated_states)
            optimal_path.append(direction)
            curr_best_node = next_node

    file.close()

if __name__ == '__main__':
    main()
