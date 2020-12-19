import sys
from mazeImageProcessor import *
from Maze import *
from MazeSolver import *
from os import path

astar = "ASTAR"
depth_first = "DEPTH FIRST"
breadth_first = "BREADTH FIRST"

#TODO: FIX image saving issues, FIX breadth-first better than a* -> PATH LENGTH?????

def main():
    #check that the file path was passed
    if len(sys.argv) != 3:
        print('invalid number of arguments passed')
        print('usage: solveMaze.py <file_path> -<search alg>')
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
    #determine the selected search algorithm
    search_algo = str(sys.argv[2])
    if search_algo.lower() == 'a*':
        search_algo = astar
    elif search_algo.lower() == 'depth-first':
        search_algo = depth_first
    elif search_algo.lower() == 'breadth-first':
        search_algo = breadth_first
    else:
        print('invalid search algorithm defined. options are:')
        print('   a*, depth-first, breadth-first')
        exit()
    #create a maze image processor object
    image_processor = mazeImageProcessor(path.abspath(file_path))
    #create the maze object from the image proccessing objects boolean maze
    maze = Maze(image_processor.boolean_maze, image_processor.width_cubes, image_processor.height_cubes)
    #print information about the maze
    maze.print_maze_data()
    #create the maze solver object
    maze_solver = MazeSolver(maze)
    #generate a path, and the path length through depth-first search
    #TODO: HERE
    if search_algo == astar:
        root, num_desc_nodes_on_path, total_path_length = maze_solver.AStar()
    elif search_algo == depth_first:
        root, num_desc_nodes_on_path, total_path_length = maze_solver.depthFirst()
    else:
        root, num_desc_nodes_on_path, total_path_length = maze_solver.breadthFirst()
    #print some information about the performance of the search alg
    maze_solver.print_maze_solve_data()
    #draw the path to the maze
    image_processor.drawPath(root, num_desc_nodes_on_path)
    #save the image
    if search_algo == astar:
        image_processor.saveSolvedMaze('SOLVED-A*')
    elif search_algo == depth_first:
        image_processor.saveSolvedMaze('SOLVED-Depth-First')
    else:
        image_processor.saveSolvedMaze('SOLVED-Breadth-First')

if __name__ == '__main__':
    main()
