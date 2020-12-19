

class mazeNode:

    def __init__(self, maze_pos_x, maze_pos_y, node_index, is_start=False, is_end=False):
        self.x = maze_pos_x
        self.y = maze_pos_y
        self.node_index = node_index
        self.is_start_node = is_start
        self.is_end_node = is_end
        self.top_neighbour = None
        self.bottom_neighbour = None
        self.left_neighbour = None
        self.right_neighbour = None
        self.next_on_path = None
        self.prev_on_path = None
        self.g = 0 if is_start else 10**1000      #used in A* algorithm
        self.f = 0 if is_start else 10**1000      #used in A* algorithm

    def set_top_neighbour(self, neighbour):
        self.top_neighbour = neighbour

    def set_bottom_neighbour(self, neighbour):
        self.bottom_neighbour = neighbour

    def set_left_neighbour(self, neighbour):
        self.left_neighbour = neighbour

    def set_right_neighbour(self, neighbour):
        self.right_neighbour = neighbour

    #returns the list of neighbours of this node
    def get_neighbours(self):
        neighbours = []
        if not self.top_neighbour == None:
            neighbours.append(self.top_neighbour)
        if not self.bottom_neighbour == None:
            neighbours.append(self.bottom_neighbour)
        if not self.left_neighbour == None:
            neighbours.append(self.left_neighbour)
        if not self.right_neighbour == None:
            neighbours.append(self.right_neighbour)
        return neighbours

    #custom comparator used in A* algorithm by the min heap open set
    def __lt__(self, other):
        return self.f < other.f

    #custom comparator used in A* algorithm by the min heap open set
    def __gt__(self, other):
        return self.f > other.f

    #return the root of the path that ends at this node and the length of that path
    #this method also makes the forward connections of all of these nodes
    def get_path_root_and_length(self):
        #loop back through the PathNodes to get the start node and make the forward connections
        num_decision_nodes = 1
        num_total_cubes_on_path = 1
        last_node = self
        while last_node.prev_on_path != None:
            num_total_cubes_on_path += last_node.get_h_score(last_node.prev_on_path)
            num_decision_nodes = num_decision_nodes + 1
            last_node.prev_on_path.next_on_path = last_node
            last_node = last_node.prev_on_path
        return last_node, num_decision_nodes, num_total_cubes_on_path

    def find_index_in_heap(self, heap):
        index = 0
        found_node = False
        for node in heap:
            if node.node_index == self.node_index:
                found_node = True
                break
            index += 1
        return index if found_node else -1

    #heuristic function -> used in A* search algorithm
    #   returns the distance from this node to other node (manhattan distance)
    def get_h_score(self, other_node):
        return abs(self.x - other_node.x) + abs(self.y - other_node.y)
