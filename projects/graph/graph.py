"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.added vertex are in a set
        """
        pass  # TODO
        self.vertices[vertex_id]=set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO
        if v1 and v2  in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Edges can't be made on the given vertices")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO
        #self.vertces["A"]=setB// it has been stored through add vertex function whosoever is the neighbor, there could be multiple, watch webpt4 lecture;time:1.25
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        pass  # TODO
        #for bft create a queue for visting all the nodes tht we want to visit and they should wait in a livne
        q= Queue()
        # to keep track of visited nodes we will make a set visited
        visited=set()
        #enque the first node in the queue
        q.enqueue(starting_vertex)
        #while queue is not empty
        while q.size()>0:
            current_node=q.dequeue()
            #check if it has been visited
            if current_node not in visited:
                #if not mark as visited
                visited.add(current_node)
                print(current_node)
                edges=self.get_neighbors(current_node)
                #put them in line to be visited
                for edge in edges:
                    q.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s= Stack()
        visited=set()
        s.push(starting_vertex)
        while s.size()>0:
            current_node=s.pop()
            if current_node  not in visited:
                visited.add(current_node)
                edges=self.get_neighbors(current_node)
                for edge in edges:
                    s.push(edge)



#First we have to add a third parameter visited=None, so that we can form a base case


    def dft_recursive(self, starting_vertex,visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO
        if visited is None:
            #then it should be an empty set,set takes .dd function to append anything
            visited=set()
        #else we have to add the first starting vertex in the visited list
        visited.add(starting_vertex)
        # since we are doing dft recursively we have to call this function again and again for each edge recursively
         #now, we will call dft recursively for the neighbors

        for neighbor in self.vertices[starting_vertex]:
            # the only thing we care that child vertex should not be  in the visited list
            if neighbor not in visited:
                self.dft_recursive(neighbor,visited)






    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        # make a queue
        # make a set for visited

        # enqueue A PATH TO the starting_vertex

        # while the queue isn't empty:
        ## dequeue the next path
        ## current_node is the last thing in the path
        ## check if it's the target, aka the destination_vertex
        ## if so, return the path!!

        ## if not, mark this as visited
        ## get the neighbors
        ## copy the path, add the neighbor to the copy
        ## for each one, add a PATH TO IT to our queue

        q= Queue()
        visited=set()
        #we will enqueue in a list... so that we could get all the possible solutions
        q.enqueue([starting_vertex])
        while q.size()>0:
            path=q.dequeue()
            current_vertex= path[-1]## get last node added to the search path
            if current_vertex not in visited:
                if current_vertex==destination_vertex:
                    return path
                #else
                visited.add(current_vertex)
                for neighbor in self.vertices[current_vertex]:
                    newPath= list(path)#copying the current path
                    newPath.append(neighbor)
                    q.enqueue(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        """
        return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO
        s = Stack()
        visited= set()
        s.push([starting_vertex])
        while s.size()>0:
           path= s.pop()
           current_vertex=path[-1]
           if current_vertex not in visited:
              if current_vertex ==destination_vertex:
                 return path
              #else add it in the visited list
              visited.add(current_vertex)
              for neighbor in self.vertices[current_vertex]:
                  newpath=list(path)#copy
                  newpath.append(neighbor)
                  s.push(newpath)




    def dfs_recursive(self, starting_vertex,destination_vertex,visited=None,path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO
        if visited==None:
            visited=set()

        if path ==None:
           path=[]

        visited.add(starting_vertex)  # add all the visited nodes
        path= path+[starting_vertex]# adding each visited node to the path
        if starting_vertex==destination_vertex:
            return path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
               new_path= self.dfs_recursive(neighbor,destination_vertex,visited, path)
               if new_path:
                  return new_path

        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
