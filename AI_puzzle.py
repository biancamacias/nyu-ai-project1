# artificial intelligence project 1
# Isabel Huey, Bianca Macias
# ijh234, bm2815
import copy

WEIGHTS = [1.0, 1.2, 1.4]
DIRECTIONS = ["L", "R", "U", "D"]

# graph search will use this Node data structure throughout
class Node:
   def __init__(self, weight, goal_state, state, direction = None, g = 0):
      self.state = state # list, current state of puzzle
      self.parent = None # None if root, must be another node otherwise
      self.weight = weight

      self.direction = direction

      self.g = g # node level
      self.h = 0 # manhattan distances from goal state, will be 0 when goal is reached
      self.f = 0 # f(n) = weight * h(n) + g(n)

      self.calculate_h(goal_state)
      self.calculate_f(weight)

   def manhattan_distance(self, goal_row, goal_column, curr_row, curr_column):
       return abs(goal_row - curr_row) + abs(goal_column - curr_column)

   def find_element(self, goal_element):
        # finds row, column of element in the current state
        # returns tuple of its location (row, column)
        for row in self.state:
            for element in row:
                if element == goal_element:
                    row_index = self.state.index(row)
                    col_index = row.index(element)
                    return row_index, col_index

   def calculate_h(self, goal_state):
        # calculates manhattan distances of curr state from goal state
        # sets h value
        total = 0
        for goal_row in goal_state:
            for goal_element in goal_row:
                curr_row, curr_column = self.find_element(goal_element)
                total += self.manhattan_distance(goal_state.index(goal_row), goal_row.index(goal_element), curr_row, curr_column)
        self.h = total

   def calculate_f(self, weight):
        # calculates and sets f value
        # self.f = weight * self.h + self.g
        self.f = self.h + self.g



   def find_empty_tile(self):
       # TODO: create helper function to find empty tile position
       # returns tuple (row, column)
       # find initial position of empty tile
       for row in self.state:
           for element in row:
               if element == '0':
                   col = row.index('0')
                   row = self.state.index(row)
                   return(row, col)
       print("Error: Cannot find empty tile")


   def move_possible(self, direction, empty_tile):
        # TODO: create helper fucnction can if can move in each direction
        # takes direction (from DIRECTIONS list)
        # returns True or False if tile can move in that direction
        (row,col) = empty_tile
        min_row = -1
        min_col = -1
        max_row = len(self.state)
        max_col = len(self.state[0])

        if direction == "U":
            up = row - 1
            if min_row < up < max_row :
                return True
            else: return False
        if direction == "D":
            down = row + 1
            if min_row < down < max_row :
                return True
            else: return False
        if direction == "L":
            left = col - 1
            if min_col < left < max_col :
                return True
            else: return False
        if direction == "R":
            right = col + 1
            if min_col < right < max_col :
                return True
            else: return False


def best_node(child_nodes, unexpanded_nodes):
    # TODO: create helper function to decide which child node is best based on f value
    # returns tuple (direction, node with lowest f value)
    min_f = -1
    direction_moved = None
    node_chosen = None
    for node in child_nodes:
        direction = node[0]
        node = node[1]
        if node!=None:
            if (min_f == -1) | (node.f < min_f):
                min_f = node.f
                direction_moved = direction
                node_chosen = node
    # Check if unexpanded nodes have a lower f value
    for unexpanded_node in unexpanded_nodes:
        if unexpanded_node.f < node_chosen.f:
            if unexpanded_node.g < node_chosen.g:
                node_chosen = unexpanded_node
    # If an unexpanded node value is chosen delete it from unexpanded node list
    if node_chosen in unexpanded_nodes:
        unexpanded_nodes.remove(node_chosen)
    # put generated nodes not chosen in unexpanded nodes list
    for node in child_nodes:
        if node[1]!= None:
            if node[1] is not node_chosen:
                unexpanded_nodes.append(node[1])

    # compare generated children's f values and unexpanded nodes f values
    return node_chosen

def move(node, direction, g, empty_tile, goal_state):
    # TODO: helper function that takes current node and creates new node where tile moves down
    # returns new node with node as its parent
    new_state = copy.deepcopy(node.state)
    weight = node.weight
    (row, col) = empty_tile
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


def generate_children(node, g, generated_states, goal_state):
    # helper function that generates valid children based on directions they can move in
    # if new child state has already been generated before, skip it (no repeated states allowed)
    # if not, add to generated_states and children list
    # returns children list
    # value of children will be None if direction is not allowed
    new_up = None
    new_down = None
    new_left = None
    new_right = None
    empty_tile = node.find_empty_tile()
    (row, col) = empty_tile
    if node.move_possible(DIRECTIONS[0], empty_tile):
        direction = (DIRECTIONS[0], col - 1)
        new_left = move(node, direction, g, empty_tile, goal_state)
        new_left.direction = DIRECTIONS[0]
        if new_left.state not in generated_states:
            generated_states.append(new_left.state)
        else:
            new_left = None
    if node.move_possible(DIRECTIONS[1], empty_tile):
        direction = (DIRECTIONS[1], col + 1)
        new_right = move(node, direction, g, empty_tile, goal_state)
        new_right.direction = DIRECTIONS[1]
        if new_right.state not in generated_states:
            generated_states.append(new_right.state)
        else:
            new_right = None
    if node.move_possible(DIRECTIONS[2], empty_tile):
        direction = (DIRECTIONS[2], row - 1)
        new_up = move(node, direction, g, empty_tile, goal_state)
        new_up.direction = DIRECTIONS[2]
        if new_up.state not in generated_states:
            generated_states.append(new_up.state)
        else:
            new_up = None
    if node.move_possible(DIRECTIONS[3], empty_tile):
        direction = (DIRECTIONS[3], row + 1)
        new_down = move(node, direction, g, empty_tile, goal_state)
        new_down.direction = DIRECTIONS[3]
        if new_down.state not in generated_states:
            generated_states.append(new_down.state)
        else:
            new_down = None
    return [("L", new_left), ("R", new_right), ("U", new_up), ("D", new_down)]

def best_move(node, g, generated_states, goal_state, unexpanded_nodes):
    # creates nodes if empty tile can move up, down, left, right
    # and if the node has not yet been created
    # sets child node parent to node
    # returns tuple (direction taken, node with best f acc to A* search)
    child_nodes = generate_children(node, g, generated_states, goal_state)
    # [up node or None, down node or None, left node or None, right node or None]
    # for node in child_nodes:
    #     print(node[0])
    #     if node[1]!= None:
    #         print(node[1].state)
    #     else: print(None)
    #     print("\n")
    return best_node(child_nodes, unexpanded_nodes)

def output(best_path, curr_best_node, initial_input, weight, g):
    for line in initial_input:
        for elem in line:
            print(elem, end=" ")
        print()
    print()
    print(weight)
    print(curr_best_node.g)
    print("N")
    for node in best_path:
        print(node.direction, end=" ")
    print()
    for node in best_path:
        print(node.f, end=" ")
    print()
    for node in best_path:
        print(node.state, end=" ")
        print(node.g, end=" ")
        print(node.f)






def main():
    # open the file
    file = open("Sample_Input.txt", "r")
    weight = WEIGHTS[0] # TODO: change this

    # puzzle state data structure: [[row 1], [row 2], [row 3]]
    initial_input = [] # initial state of puzzle
    goal_state = [] # will hold goal state, input from input file
    generated_states = [] # list to hold states already created to prevent repeated states
    g = 0 # g(n) value, root starts at 0

    # Make a list
    for line in file:
        line = line.strip()
        line = line.split(' ')
        initial_input.append(line)

    # current state
    curr_state = initial_input[0:3]

    # goal state
    goal_state = initial_input[4:8]

    # create root, then start generating graph tree
    root = Node(weight, goal_state, curr_state, None, g)
    generated_states.append(root.state)
    # goal_reached = False
    curr_best_node = root
    unexpanded_nodes = []
    best_path =[]
    # import pdb; pdb.set_trace()
    while (curr_best_node!= None) & (curr_best_node.state != goal_state):
        g += 1
        next_node = best_move(curr_best_node, g, generated_states, goal_state, unexpanded_nodes)
        curr_best_node = next_node
        # for node in best_path:
        #     if node.g != 1:
        #         if node.g >= curr_best_node.g:
        #             best_path.remove(node)
        g = curr_best_node.g
        best_path.append(curr_best_node)
    output(best_path, curr_best_node, initial_input, weight, g)


    file.close()

if __name__ == '__main__':
    main()
