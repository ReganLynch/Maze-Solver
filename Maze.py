
from mazeNode import *

class Maze:

    def __init__(self, boolean_maze, maze_width, maze_height):
        self.boolean_maze = boolean_maze
        self.maze_width = maze_width
        self.maze_height = maze_height
        self.start_node = None
        self.end_node = None
        self.find_decision_nodes()

    #algorithm for generating only the essential decision nodes of this maze
    def find_decision_nodes(self):
        #first find start and end nodes
        for i in range(0, self.maze_width):
            #if found start
            if self.boolean_maze[0][i]:
                self.start_node = mazeNode(i, 0, is_start=True)
            #if found end
            elif self.boolean_maze[self.maze_height-1][i]:
                self.end_node = mazeNode(i, self.maze_height-1, is_end=True)
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
        #---now find all escential nodes----
        #loop down each column
        for y in range(1, self.maze_height):
            #loop across each row
            for x in range(0, self.maze_width - 1):
                print()
