from PIL import Image
from mazeNode import *
from os import path

class mazeImageProcessor:

    BLACK = (0,0,0)
    WHITE = (255,255,255)

    def __init__(self, maze_file_path):
        self.in_file_path = maze_file_path
        self.pil_image = Image.open(self.in_file_path).convert('RGB')
        self.pixels = self.pil_image.load()
        self.width_px, self.height_px = self.pil_image.size
        self.findCubeSize()
        self.findMazeDimentions()
        self.createMazeBooleanArray()

    #determine the size of the cubes in this maze (based on the size of the start position)
    def findCubeSize(self):
        self.cube_size = 0
        for i in range(0, self.width_px):
            if self.pixels[i,0] == mazeImageProcessor.WHITE:
                self.cube_size = self.cube_size + 1

    #determines the dimentions of the maze, in cubes
    def findMazeDimentions(self):
        self.width_cubes = int(self.width_px/self.cube_size) - 1  ## TODO: shouldnt have to minus 1 from this
        self.height_cubes = int(self.height_px/self.cube_size) - 1 ## TODO: shouldne have to minus 1 from this

    #generates a boolean array, which represents the maze (false for wall, true for path)
    def createMazeBooleanArray(self):
        self.boolean_maze = [[False for i in range(self.width_cubes)] for j in range(self.height_cubes)]
        for i in range(0, self.width_cubes):
            for j in range(0, self.height_cubes):
                image_x_pos = self.cube_size * i
                image_y_pos = self.cube_size * j
                if self.pixels[image_x_pos,image_y_pos] == mazeImageProcessor.WHITE:
                    self.boolean_maze[j][i] = True

    #fills in a cube section with a colour, based on the cube size
    def fillMazeCubeSection(self, x, y, colour):
        real_x = x * self.cube_size
        real_y = y * self.cube_size
        for i in range(0, self.cube_size):  #x axis
            for j in range(0, self.cube_size):  #x axis
                curr_x = real_x + i
                curr_y = real_y + j
                self.pixels[curr_x, curr_y] = colour

    #fills in the section of a maze between two mazeNode objects with a certain colour
    def fillMazeConnection(self, maze_node_a, maze_node_b, colour):
        start_node = None
        end_node = None
        #if they are vertical to eachother
        if maze_node_a.x == maze_node_b.x:
            if maze_node_a.y > maze_node_b.y:
                start_node = maze_node_b
                end_node = maze_node_a
            else:
                start_node = maze_node_a
                end_node = maze_node_b
            #fill in the vertical tiles
            for i in range(start_node.y + 1, end_node.y):
                self.fillMazeCubeSection(start_node.x, i, colour)
        #if they are horizontal to eachother
        else:
            if maze_node_a.x > maze_node_b.x:
                start_node = maze_node_b
                end_node = maze_node_a
            else:
                start_node = maze_node_a
                end_node = maze_node_b
            #fill in the horizontal tiles
            for i in range(start_node.x + 1, end_node.x):
                self.fillMazeCubeSection(i, start_node.y, colour)

    #draws a path to the maze, from the root of the path, to the end. colours in the path with a gradient from green to red
    def drawPath(self, path_root_node, path_length):
        prev_node = None
        curr_node = path_root_node
        curr_node_index = 0
        colour_step_size = 255 / path_length
        while curr_node != None:
            #increment the current node index
            curr_node_index = curr_node_index + 1
            #calculate the colour value factor
            colour_val_factor = int(255 * (curr_node_index / path_length))
            #if on first node, just draw the node
            if prev_node == None:
                self.fillMazeCubeSection(curr_node.x, curr_node.y, (colour_val_factor, 255 - colour_val_factor, 0))
            #if on any other node, draw the node, and the connection to the previous node
            else:
                self.fillMazeCubeSection(curr_node.x, curr_node.y, (colour_val_factor, 255 - colour_val_factor, 0))
                self.fillMazeConnection(prev_node, curr_node, (colour_val_factor, 255 - colour_val_factor, 0))
            #set the previous node to the current node
            prev_node = curr_node
            curr_node = curr_node.next_on_path

    #saves the maze
    def saveSolvedMaze(self, out_file_name):
        file_name, file_extension = path.splitext(self.in_file_path)
        self.pil_image.save(file_name + '_' + out_file_name + '_'+ file_extension)
