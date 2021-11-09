# cs-uy 4613 artificial intelligence project 1
# Isabel Huey, Bianca Macias
# ijh234, bm2815
import copy

# Node is a unique tile arrangement that holds state, parent node, weight,
# direction taken to get to the tile arrangement, g, h, and f
class Node:
    def __init__(self, weight, goal_state, state, direction = None, g = 0):
        self.state = state # list, current state of puzzle
        self.parent = None # None if root, another Node otherwise
        self.weight = weight # weight (integer) inputted by user

        self.direction = direction # "L", "R", "U", or "D"

        self.g = g # node level
        self.h = 0 # manhattan distances from goal state, 0 when goal is reached
        self.f = 0 # f(n) = weight * h(n) + g(n)

        self.calculate_h(goal_state) # call function to set h
        self.calculate_f(weight) # call function to set f

    # Method to calculate manhattan distances of the current tile
    # Takes in the goal position and the current position
    # Returns individual manhattan distance (integer)
    def manhattan_distance(self, goal_row, goal_column, curr_row, curr_column):
        return abs(goal_row - curr_row) + abs(goal_column - curr_column)

    # Method that finds row, column of element in the current state
    # returns tuple of its location as indices (row, column)
    def find_element(self, element_to_find):
        for row in self.state:
            for element in row:
                if element == element_to_find:
                    curr_row = self.state.index(row)
                    curr_col = row.index(element)
                    return curr_row, curr_col

    # Method calculates manhattan distances of current state from goal state
    # sets h attribute
    def calculate_h(self, goal_state):
        total = 0
        for goal_row in goal_state:
            for goal_element in goal_row:
                curr_row, curr_column = self.find_element(goal_element)
                total += self.manhattan_distance(goal_state.index(goal_row), \
                         goal_row.index(goal_element), curr_row, curr_column)
        self.h = total

    # Method calculates and sets f attribute
    def calculate_f(self, weight):
        self.f = round((weight* self.h + self.g), 1)

    # Method to find empty tile position
    # returns tuple (row, column)
    def find_empty_tile(self):
        for row in self.state:
           for element in row:
               if element == '0':
                   col = row.index('0')
                   row = self.state.index(row)
                   return row, col

    # Method that checks if empty tile can move in given direction
    # returns True or False if tile can move in that direction
    def move_possible(self, direction, d_index, empty_tile):
        row, col = empty_tile
        min_row = -1
        min_col = -1
        max_row = len(self.state)
        max_col = len(self.state[0])

        if (direction == "U") | (direction == "D"):
            if min_row < d_index < max_row:
                return True
            else: return False
        if (direction == "L") | (direction == "R"):
            if min_col < d_index < max_col:
                return True
            else: return False

# Helper function to decide which child node is best based on f value
# The node is best if it has the lowest f value out of all the unexpanded nodes
# returns tuple (direction, Node with lowest f value)
def best_node(child_nodes, frontier):
    min_f = -1
    direction_moved = None
    node_chosen = None
    for node in child_nodes: # node = (direction (string), Node or none)
        direction = node[0]
        node = node[1]
        if node != None:
            if (min_f == -1) | (node.f < min_f):
                min_f = node.f
                direction_moved = direction
                node_chosen = node
    # Check if unexpanded nodes have a lower f value
    # Iterate through the reverse of the frontier
    # because A* search has a LIFO frontier
    for leaf_node in reversed(frontier):
        if leaf_node.f < node_chosen.f:
            if leaf_node.g < node_chosen.g:
                node_chosen = leaf_node
    # If an unexpanded node value is chosen, delete it from frontier
    # because it will now be an expanded node
    if node_chosen in frontier:
        frontier.remove(node_chosen)
    # Put generated nodes not chosen into frontier
    for node in child_nodes:
        if node[1] != None:
            if node[1] is not node_chosen:
                frontier.append(node[1])
    return node_chosen

# Helper function that takes current node, direction, g, empty_tile position,
# and goal_state
# moves the empty tile accordingly
# returns a new Node with the current node as its parent
def move(node, direction, g, empty_tile, goal_state):
    new_state = copy.deepcopy(node.state)
    weight = node.weight
    row, col = empty_tile
    if (direction[0] == "U") | (direction[0] == "D"):
        new_row = direction[1]
        new_state[row][col] = new_state[new_row][col]
        new_state[new_row][col] = '0'
    else:
        new_col = direction[1]
        new_state[row][col] = new_state[row][new_col]
        new_state[row][new_col] = '0'
    new_node = Node(weight, goal_state, new_state, None, g)
    new_node.parent = node
    return new_node

# Helper function to create a new node based on a direction
# Returns a new Node object
def create_node(node, direction, g, empty_tile, goal_state, generated_states):
    new_node = move(node, direction, g, empty_tile, goal_state)
    new_node.direction = direction[0]
    if new_node.state not in generated_states:
        generated_states.append(new_node.state)
    else:
        new_node = None
    return new_node

# Helper function that generates valid children based on directions
# they can move in
# if new child state has already been generated before,
# skip it (no repeated states allowed)
# if not, add to generated_states and children list
# returns children list
# value of children will be None if direction is not allowed
def generate_children(node, g, generated_states, goal_state):
    new_left, new_right, new_up, new_down = None, None, None, None
    empty_tile = node.find_empty_tile()
    (row, col) = empty_tile
    left_index, right_index = col - 1, col + 1
    up_index, down_index = row - 1, row + 1
    if node.move_possible("L", left_index, empty_tile):
        direction = ("L", left_index)
        new_left = create_node(node, direction, g, empty_tile, goal_state, generated_states)
    if node.move_possible("R", right_index, empty_tile):
        direction = ("R", right_index)
        new_right = create_node(node, direction, g, empty_tile, goal_state, generated_states)
    if node.move_possible("U", up_index, empty_tile):
        direction = ("U", up_index)
        new_up = create_node(node, direction, g, empty_tile, goal_state, generated_states)
    if node.move_possible("D", down_index, empty_tile):
        direction = ("D", down_index)
        new_down = create_node(node, direction, g, empty_tile, goal_state, generated_states)
    return [("L", new_left), ("R", new_right), ("U", new_up), ("D", new_down)]

# Function that creates nodes if empty tile can move up, down, left, right
# and if the node has not yet been created
# sets child node parent to node
# returns the next node to be expanded
def best_move(node, g, generated_states, goal_state, frontier):
    child_nodes = generate_children(node, g, generated_states, goal_state)
    # [("L", Node or None), ("R", Node or None),
    #  ("U", Node or None), ("D", Node or None)]
    return best_node(child_nodes, frontier)

# Print output in the correct format
def output(best_path, curr_best_node, initial_input, weight, g, num_nodes):
    for line in initial_input:
        for elem in line:
            print(elem, end = " ")
        print()
    print()
    print(weight)
    print(curr_best_node.g)
    print(num_nodes)
    for node in best_path:
        print(node.direction, end=" ")
    print()
    for node in best_path:
        print(node.f, end=" ")
    print()

def main():
    # Ask for input to obtain filename and try to open the file
    file = None
    while file == None:
        filename = input("Enter the name of the input file: ")
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("File not found, try again")
    # Ask for input to obtain weighted value
    weight = float(input("Enter the weight (W) for the heuristic function: "))

    # puzzle state data structure: [[row 1], [row 2], [row 3]]
    initial_input = [] # input in list format
    generated_states = [] # list to hold states created to prevent repeated states
    frontier = [] # initialize empty list for LIFO frontier
    best_path =[] # intialize empty list to store best node path
    g = 0 # g(n) value, root starts at 0

    # Make a list of the initial input from the input file
    for line in file:
        line = line.strip()
        line = line.split(' ')
        initial_input.append(line)

    # Seperate initial input into the initial state and the goal state
    # current state
    curr_state = initial_input[0:3]
    # goal state
    goal_state = initial_input[4:8]

    # create root Node and add Node to generated states
    root = Node(weight, goal_state, curr_state, None, g)
    generated_states.append(root.state)

    # initialize Node pointer
    curr_best_node = root

    # while the current state does not equal the goal state, traverse graph
    while (curr_best_node.state != goal_state):
        g += 1
        next_node = best_move(curr_best_node, g, generated_states, goal_state, frontier)
        curr_best_node = next_node
        g = curr_best_node.g
    # goal_node is a copy of curr_best_node
    goal_node = copy.deepcopy(curr_best_node)
    best_path = [] #intiialize best_path empty list
    # while final state is not equal to root state
    # find the correct parent node of the current nodes
    # and append it to best_path list to get the correct
    # reversed node path
    while (goal_node.state != root.state):
        if goal_node!= None:
            best_path.append(goal_node)
            goal_node = goal_node.parent
    # reverse the list of nodes representing the best node path in order to
    # have the correct order from root to goal node
    best_path.reverse()
    # call output to print the results in the correct format
    output(best_path, curr_best_node, initial_input, weight, g, len(generated_states))

    # close the file used
    file.close()

if __name__ == '__main__':
    main()
