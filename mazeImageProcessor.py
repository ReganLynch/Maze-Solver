from PIL import Image
from os import path

class mazeImageProcessor:

    BLACK = (0,0,0,255)
    WHITE = (255,255,255,255)

    def __init__(self, maze_file_path):
        self.in_file_path = maze_file_path
        file_name, file_extension = path.splitext(maze_file_path)
        self.out_file_path = file_name + '_SOLVED' + file_extension
        self.pil_image = Image.open(self.in_file_path)
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
        self.width_cubes = (self.width_px - (2*self.cube_size)) / (2 * self.cube_size)
        self.heigh_cubes = (self.height_px - (2*self.cube_size)) / (2 * self.cube_size)

    #generates a boolean array, which represents the maze (false for wall, true for path)
    def createMazeBooleanArray(self):
        self.boolean_maze = [[False for i in range(self.width_cubes)] for j in range(self.heigh_cubes)]

    #saves the maze
    def saveSolvedMaze(self):
        self.pil_image.save(self.out_file_path)
