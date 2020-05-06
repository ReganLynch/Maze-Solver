from mazeNode import *

class MazeSolver:

    def __init__(self, maze):
        self.maze = maze
        self.visited = [False for i in range (0, self.maze.num_nodes)]

    #performs a depht-first search on the maze, and returns the root node of a path
    def depthFirst(self):
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
        #loop back through the PathNodes to get the start node and make the forward connections
        path_length = 1
        while last_node.prev_on_path != None:
            path_length = path_length + 1
            last_node.prev_on_path.next_on_path = last_node
            last_node = last_node.prev_on_path
        return last_node, path_length

    def breadthFirst(self):
        return 1

    def AStar(self):
        return 1
