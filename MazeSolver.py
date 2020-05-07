from mazeNode import *
import datetime
from collections import deque

class MazeSolver:

    def __init__(self, maze):
        self.maze = maze
        self.visited = [False for i in range (0, self.maze.num_nodes)]

    #performs a depth-first search on the maze, and returns the root node of a path
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
                    stack.append(curr_maze_node.top_neighbour)
                    if curr_maze_node.top_neighbour.prev_on_path == None:
                        curr_maze_node.top_neighbour.prev_on_path = curr_maze_node
                if curr_maze_node.bottom_neighbour != None:
                    stack.append(curr_maze_node.bottom_neighbour)
                    if curr_maze_node.bottom_neighbour.prev_on_path == None:
                        curr_maze_node.bottom_neighbour.prev_on_path = curr_maze_node
                if curr_maze_node.left_neighbour != None:
                    stack.append(curr_maze_node.left_neighbour)
                    if curr_maze_node.left_neighbour.prev_on_path == None:
                        curr_maze_node.left_neighbour.prev_on_path = curr_maze_node
                if curr_maze_node.right_neighbour != None:
                    stack.append(curr_maze_node.right_neighbour)
                    if curr_maze_node.right_neighbour.prev_on_path == None:
                        curr_maze_node.right_neighbour.prev_on_path = curr_maze_node
        #make sure that the start node has no previous node on path
        self.maze.start_node.prev_on_path = None
        #reset the visited array
        self.visited = [False for i in range (0, self.maze.num_nodes)]
        #return the root node and the path length of the path that ends at last_node
        ret = last_node.get_path_root_and_length()
        #set the time it took to perform dfs
        self.solve_end_time = datetime.datetime.now()
        self.num_nodes_on_solved_path = ret[1]
        return ret

    #performs a breadth-first search on the maze, and returns the root node of a path
    def breadthFirst(self):
        #initialize the start_time of the solve
        self.solve_start_time = datetime.datetime.now()
        self.most_recent_search_alg = 'Breadth-first'
        #--perform breadth-first search--
        queue = deque()
        self.visited[self.maze.start_node.node_index] = True
        queue.append(self.maze.start_node)
        last_node = None
        while queue:
            curr_node = queue.popleft()
            if curr_node.node_index == self.maze.end_node.node_index:
                last_node = curr_node
                break
            #add all nodes connected to this node
            if curr_node.top_neighbour != None:
                if not self.visited[curr_node.top_neighbour.node_index]:
                    queue.append(curr_node.top_neighbour)
                    curr_node.top_neighbour.prev_on_path = curr_node
                    self.visited[curr_node.top_neighbour.node_index] = True
            if curr_node.bottom_neighbour != None:
                if not self.visited[curr_node.bottom_neighbour.node_index]:
                    queue.append(curr_node.bottom_neighbour)
                    curr_node.bottom_neighbour.prev_on_path = curr_node
                    self.visited[curr_node.bottom_neighbour.node_index] = True
            if curr_node.left_neighbour != None:
                if not self.visited[curr_node.left_neighbour.node_index]:
                    queue.append(curr_node.left_neighbour)
                    curr_node.left_neighbour.prev_on_path = curr_node
                    self.visited[curr_node.left_neighbour.node_index] = True
            if curr_node.right_neighbour != None:
                if not self.visited[curr_node.right_neighbour.node_index]:
                    queue.append(curr_node.right_neighbour)
                    curr_node.right_neighbour.prev_on_path = curr_node
                    self.visited[curr_node.right_neighbour.node_index] = True
        #make sure that the start node has no previous node on path
        self.maze.start_node.prev_on_path = None
        #reset the visited array
        self.visited = [False for i in range (0, self.maze.num_nodes)]
        #return the root node and the path length of the path that ends at last_node
        ret = last_node.get_path_root_and_length()
        #set the time it took to perform bfs
        self.solve_end_time = datetime.datetime.now()
        self.num_nodes_on_solved_path = ret[1]
        return ret

    def AStar(self):
        #initialize the start_time of the solve
        self.solve_start_time = datetime.datetime.now()
        self.most_recent_search_alg = 'A*'
        #perform A* algorithm search
        #--------here-------------
        #reset the visited array
        self.visited = [False for i in range (0, self.maze.num_nodes)]
        #return the root node and the path length of the path that ends at last_node
        #ret = last_node.get_path_root_and_length()
        #set the time it took to perform bfs
        self.solve_end_time = datetime.datetime.now()
        #self.num_nodes_on_solved_path = ret[1]
        return 1

    def print_maze_solve_data(self):
        elapsed_time = self.solve_end_time - self.solve_start_time
        print(self.most_recent_search_alg, ' search path finding results...')
        print('Number of nodes on found path: ', self.num_nodes_on_solved_path)
        print('Time taken to find path: ', elapsed_time.total_seconds(), ' seconds')
