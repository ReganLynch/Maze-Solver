# MazeSolver
python script that finds the path through a maze.

## How To Use
  ```shell
  pyhton3 solveMaze.py <input image> <search algorithm>
  ```
  - first argument is a '.bmp' image generated from my [Javascript Maze Generator](https://github.com/ReganLynch/Maze-Generator)
  - second argument is the desired search algorithm to be used. Available algorithms are:
    - a*
    - depth-first
    - breadth-first
  
  ## Example Input-Output
   ```shell
   python3 solveMaze.py ./input-mazes/100x100-5px.bmp a*
   ```
   - will create a new '.bmp' file in the same folder as the origial image, displaying the path the A* algorithm found through the input maze.
   - key information about the maze, and the path found will also be printed to console.
   
   ### Example Input Image
   ![Input Image](https://github.com/ReganLynch/Maze-Solver/blob/master/input-mazes/100x100-5px.bmp)
   
   ### Example Output Image - A*
   ![Output Image](https://github.com/ReganLynch/Maze-Solver/blob/master/input-mazes/100x100-5px_SOLVED-A*_.bmp)
