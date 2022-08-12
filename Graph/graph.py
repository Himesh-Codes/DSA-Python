"""
Graph data structure is a collection of nodes that have data and are connected to other nodes.

More precisely, a graph is a data structure (V, E) that consists of

 - A collection of vertices V (all vertices or nodes)
 - A collection of edges E, represented as ordered pairs of vertices (u,v) , (represents the connections)
 
 Graph Terminology
    - Adjacency: A vertex is said to be adjacent to another vertex if there is an edge connecting them.
    - Path: A sequence of edges that allows you to go from vertex A to vertex B is called a path. 
    - Directed Graph: A graph in which an edge (u,v) doesn't necessarily mean that there is an edge (v, u) as well. 
        The edges in such a graph are represented by arrows to show the direction of the edge.
        
Graph Representation
    Graphs are commonly represented in two ways:

    1. Adjacency Matrix
    2. Adjacency List
        An adjacency list represents a graph as an array of linked lists.
    
    Graph Operations
    The most common graph operations are:

     - Check if the element is present in the graph
     - Graph Traversal
     - Add elements(vertex, edges) to graph
     - Finding the path from one vertex to another
     
Spanning Tree and Minimum Spanning Tree
 - Spanning tree
    A spanning tree is a sub-graph of an undirected connected graph, which includes all the vertices of the
    graph with a minimum possible number of edges. If a vertex is missed, then it is not a spanning tree.
    The total number of spanning trees with n vertices that can be created from a complete graph is equal to n(n-2).
 - Minimum Spanning Tree
    A minimum spanning tree is a spanning tree in which the sum of the weight of the edges is as 
    minimum as possible.
    Spanning Tree Applications
    --------------------------------
        - Computer Network Routing Protocol
        - Cluster Analysis
        - Civil Network Planning
"""

from collections import defaultdict

class Graph():
    def __init__(self, numofvertex):
        self.__numofvertex = numofvertex
        self.__graph = defaultdict(list)
    
    def addEdge(self, start, destination):
        self.__graph[start].append(destination)
        
    # keep log of visited nodes & traverse through the nodes untill every nodes visited
    # It goes from start to max end and back track to root and visit next route
    def dfs(self, startVertex, visitedNodes=None):
        if visitedNodes == None:
            visitedNodes = list()
        visitedNodes.append(startVertex)
        
        for next in self.__graph[startVertex]:
            if next not in visitedNodes:
                self.dfs(next, visitedNodes)
        return visitedNodes
    
    # bfs always have visited array and not visited queue
    # adjacent vertex items pushed to queue and visit the items of queue from front
    def bfs(self, startVetex, visited: list = None, notVisited: list = None):
        if visited == None and notVisited == None:
            visited = list()
            notVisited = list()
        # add each visited node
        visited.append(startVetex)
        # The adjacent vertices should not be visited rather not already presented in notVisited
        filteredAdjacents = [item for item in self.__graph[startVetex] if item not in visited and item not in notVisited]
        # add new array to end of array
        notVisited.extend(filteredAdjacents)
        
        # while every nodes visited
        while len(notVisited) > 0:
            nextVertex = notVisited[0]
            if nextVertex and nextVertex not in visited:
                notVisited.pop(0)
                self.bfs(nextVertex, visited, notVisited)
        return visited
    
# Testing
graph = Graph(5)
graph.addEdge(0, 1)
graph.addEdge(1, 3)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(3, 4)
graph.addEdge(0, 3)

print(graph.dfs(1))
print(graph.dfs(3))
print(graph.dfs(4))

print('-----BFS-----')
print(graph.bfs(0))