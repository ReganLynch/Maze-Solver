from PIL import Image
from os import path

class mazeImageProcessor:

    BLACK = (0,0,0)
    WHITE = (255,255,255)

    def __init__(self, maze_file_path):
        self.in_file_path = maze_file_path
        file_name, file_extension = path.splitext(maze_file_path)
        self.out_file_path = file_name + '_SOLVED' + file_extension
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
    def fillMazeCubeSection(self, x_pos, y_pos, colour):
        real_x = x_pos * self.cube_size
        real_y = y_pos * self.cube_size
        for i in range(0, self.cube_size):  #x axis
            for j in range(0, self.cube_size):  #x axis
                curr_x = real_x + i
                curr_y = real_y + j
                self.pixels[curr_x, curr_y] = colour

    #saves the maze
    def saveSolvedMaze(self):
        self.pil_image.save(self.out_file_path)
