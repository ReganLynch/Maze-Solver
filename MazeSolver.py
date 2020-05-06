from mazeNode import *
import datetime

class MazeSolver:

    def __init__(self, maze):
        self.maze = maze
        self.visited = [False for i in range (0, self.maze.num_nodes)]

    #performs a depht-first search on the maze, and returns the root node of a path
    def depthFirst(self):
        #initialize the start_time of the solve
        self.solve_start_time = datetime.datetime.now()
        self.most_recent_search_alg = 'Depth-first'
        #begin depth-first search
        stack = []
        stack.append(self.maze.start_node)
        last_node = None
        #while the stack is not empty
        while stack:
            curr_maze_node = stack.pop()
            #check if we have reached out end node
            if curr_maze_node.node_index == self.maze.end_node.node_index:
                last_node = curr_maze_node
                break
            #if the current node has not been visited
            if not self.visited[curr_maze_node.node_index]:
                #mark this node as having been visited
                self.visited[curr_maze_node.node_index] = True
                #add all connected nodes to the stack
                if curr_maze_node.top_neighbour != None:
                    if not self.visited[curr_maze_node.top_neighbour.node_index]:
                        stack.append(curr_maze_node.top_neighbour)
                        curr_maze_node.top_neighbour.prev_on_path = curr_maze_node
                if curr_maze_node.bottom_neighbour != None:
                    if not self.visited[curr_maze_node.bottom_neighbour.node_index]:
                        stack.append(curr_maze_node.bottom_neighbour)
                        curr_maze_node.bottom_neighbour.prev_on_path = curr_maze_node
                if curr_maze_node.left_neighbour != None:
                    if not self.visited[curr_maze_node.left_neighbour.node_index]:
                        stack.append(curr_maze_node.left_neighbour)
                        curr_maze_node.left_neighbour.prev_on_path = curr_maze_node
                if curr_maze_node.right_neighbour != None:
                    if not self.visited[curr_maze_node.right_neighbour.node_index]:
                        stack.append(curr_maze_node.right_neighbour)
                        curr_maze_node.right_neighbour.prev_on_path = curr_maze_node
        #reset the visited array
        self.visited = [False for i in range (0, self.maze.num_nodes)]
        #return the root node and the path length of the path that ends at last_node
        ret = last_node.get_path_root_and_length()
        #set the time it took to perform dfs
        self.solve_end_time = datetime.datetime.now()
        self.num_nodes_on_solved_path = ret[1]
        return ret

    def breadthFirst(self):
        return 1

    def AStar(self):
        return 1

    def print_maze_solve_data(self):
        elapsed_time = self.solve_end_time - self.solve_start_time
        print(self.most_recent_search_alg, ' search path finding results...')
        print('Number of nodes on found path: ', self.num_nodes_on_solved_path)
        print('Time taken to find path: ', elapsed_time.total_seconds(), ' seconds')
