

class mazeNode:

    def __init__(self, maze_pos_x, maze_pos_y, node_index, is_start=False, is_end=False):
        self.x = maze_pos_x
        self.y = maze_pos_y
        self.node_index = node_index
        self.is_start_node = is_start
        self.is_end_node = is_end
        self.neighbours = []
        self.top_neighbour = None
        self.bottom_neighbour = None
        self.left_neighbour = None
        self.right_neighbour = None
        self.next_on_path = None
        self.prev_on_path = None

    def set_top_neighbour(self, neighbour):
        self.top_neighbour = neighbour

    def set_bottom_neighbour(self, neighbour):
        self.bottom_neighbour = neighbour

    def set_left_neighbour(self, neighbour):
        self.left_neighbour = neighbour

    def set_right_neighbour(self, neighbour):
        self.right_neighbour = neighbour

    #return the root of the path that ends at this node and the length of that path
    #this method also makes the forward connections of all of these nodes
    def get_path_root_and_length(self):
        #loop back through the PathNodes to get the start node and make the forward connections
        path_length = 1
        last_node = self
        while last_node.prev_on_path != None:
            path_length = path_length + 1
            last_node.prev_on_path.next_on_path = last_node
            last_node = last_node.prev_on_path
        return last_node, path_length
