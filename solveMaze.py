import sys
from mazeImageProcessor import *
from Maze import *
from MazeSolver import *
from os import path


def main():
    #check that the file path was passed
    if len(sys.argv) != 2:
        print('invalid number of arguments passed')
        print('usage: solveMaze.py <file_path>')
        exit()
    file_path = str(sys.argv[1])
    #check if the passed file is valid
    if not path.exists(file_path):
        print('invalid file path')
        exit()
    #check that the input file is a .bmp
    file_name, file_extension = path.splitext(file_path)
    if(file_extension != '.bmp' and file_extension != '.BMP'):
        print('invalid file path')
        exit()
    #create a maze image processor object
    image_processor = mazeImageProcessor(path.abspath(file_path))
    #create the maze object from the image proccessing objects boolean maze
    maze = Maze(image_processor.boolean_maze, image_processor.width_cubes, image_processor.height_cubes)
    #create the maze solver object
    maze_solver = MazeSolver(maze)
    #generate a path, and the path length through depth-first search
    root, path_length = maze_solver.depthFirst()

    #draw the path to the maze
    image_processor.drawPath(root, path_length)
    #save the image
    image_processor.saveSolvedMaze('TEST')

if __name__ == '__main__':
    main()
