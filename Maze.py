import datetime
from mazeNode import *

class Maze:

    def __init__(self, boolean_maze, maze_width, maze_height):
        self.boolean_maze = boolean_maze
        self.maze_width = maze_width
        self.maze_height = maze_height
        self.start_node = None
        self.end_node = None
        self.num_nodes = 0
        #generate the desicion nodes and keep track of the time it took to generate that data
        self.generation_start_time = datetime.datetime.now()
        self.find_decision_nodes()
        self.generation_end_time = datetime.datetime.now()
        self.generation_time_elapsed = self.generation_end_time - self.generation_start_time

    #algorithm for generating only the essential decision nodes of this maze
    def find_decision_nodes(self):
        #first find start and end nodes (check top, bottom, then left and right sides of maze)
        #   search top and bottom (top is start, bottom is end)
        for i in range(0, self.maze_width):
            #if found start on top
            if self.boolean_maze[0][i]:
                self.start_node = mazeNode(i, 0, 0, is_start=True)
            #if found end on bottom
            elif self.boolean_maze[self.maze_height-1][i]:
                self.end_node = mazeNode(i, self.maze_height-1, 1, is_end=True)
        #   search left and right (left is start, right is end)
        for i in range(0, self.maze_height):
            #if found start on left
            if self.boolean_maze[i][0]:
                self.start_node = mazeNode(0, i, 0, is_start=True)
            #if found end on right
            elif self.boolean_maze[i][self.maze_width-1]:
                self.end_node = mazeNode(self.maze_width-1, i, 1, is_end=True)
        #validate that the start and end nodes where found
        err = False
        if self.start_node == None and self.end_node == None:
            print('no start or end nodes were found in this maze, cannot solve maze')
            err = True
        elif self.start_node == None:
            print('no start node found, cannot solve maze')
            err = True
        elif self.end_node == None:
            print('no end node found, cannot solve maze')
            err = True
        #exit if either of the start or ends nodes were not found
        if err:
            exit()
        #set the number of nodes
        self.num_nodes = 2
        #---now find all escential nodes----
        #initialize the previous vertical nodes array
        prev_vertical_nodes = [None for i in range(0, self.maze_width)]
        #loop down each column
        for y in range(1, self.maze_height - 1):
            prev_horizontal_node = None
            #loop across each row
            for x in range(1, self.maze_width - 1):
                is_path = self.boolean_maze[y][x]
                #first check if we are on a wall
                if not is_path:
                    prev_horizontal_node = None
                    prev_vertical_nodes[x] = None
                #check the sides of this tile
                top_is_path = self.boolean_maze[y-1][x]
                bottom_is_path = self.boolean_maze[y+1][x]
                left_is_path = self.boolean_maze[y][x-1]
                right_is_path = self.boolean_maze[y][x+1]
                is_decision_node = False
                #check if a right turn from below
                if is_path and bottom_is_path and right_is_path:
                    is_decision_node = True
                #check if left turn from below
                elif is_path and bottom_is_path and left_is_path:
                    is_decision_node = True
                #check if right turn from top
                elif is_path and top_is_path and right_is_path:
                    is_decision_node = True
                #check if left turn from top
                elif is_path and top_is_path and left_is_path:
                    is_decision_node = True
                #if the node was found to be a decision node
                if is_decision_node:
                    #set the current node
                    curr_node = mazeNode(x, y, self.num_nodes)
                    #increment the number of nodes
                    self.num_nodes = self.num_nodes + 1
                    #make horizontal connection
                    if not prev_horizontal_node == None:
                        curr_node.set_left_neighbour(prev_horizontal_node)
                        prev_horizontal_node.set_right_neighbour(curr_node)
                    #make vertical connection
                    if not prev_vertical_nodes[x] == None:
                        curr_node.set_top_neighbour(prev_vertical_nodes[x])
                        prev_vertical_nodes[x].set_bottom_neighbour(curr_node)

                    #TODO: FIX
                    #check if this node connects to the end node
                    if curr_node.x == self.start_node.x and curr_node.y == self.start_node.y + 1:  #if connected to start node (TOP)
                        self.start_node.set_bottom_neighbour(curr_node)
                        curr_node.set_top_neighbour(self.start_node)
                    elif curr_node.x == self.start_node.x + 1 and curr_node.y == self.start_node.y:
                        self.start_node.set_right_neighbour(curr_node)
                        curr_node.set_left_neighbour(self.start_node)
                    #check if this node connects to the end node
                    elif curr_node.x == self.end_node.x and curr_node.y == self.end_node.y - 1:  #if connected to end node (BOTTOM)
                        self.end_node.set_top_neighbour(curr_node)
                        curr_node.set_bottom_neighbour(self.end_node)
                    elif curr_node.x == self.end_node.x - 1 and curr_node.y == self.end_node.y:
                        self.end_node.set_left_neighbour(curr_node)
                        curr_node.set_right_neighbour(self.end_node)

                    #set the previous vertical node
                    prev_vertical_nodes[x] = curr_node
                    #set the previous horizontal node
                    prev_horizontal_node = curr_node

    def print_maze_data(self):
        print('Number of decision nodes found in maze: ', self.num_nodes)
        print('Time spent creating graph from input maze: ', self.generation_time_elapsed.total_seconds(), ' seconds')
