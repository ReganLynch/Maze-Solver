

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
