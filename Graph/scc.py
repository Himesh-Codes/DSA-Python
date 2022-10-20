"""
SCC - Strongly connected components
A strongly connected component is the portion of a directed graph in which 
there is a path from each vertex to another vertex
You can observe that in the first strongly connected component, 
every vertex can reach the other vertex through the directed path.

Kosaraju's Algorithm
---------------------------
Kosaraju's Algorithm is based on the depth-first search algorithm implemented twice.

Three steps are involved.

1.Perform a depth first search on the whole graph.
2.Reverse the original graph.
3.Perform depth-first search on the reversed graph.
4.Thus, the strongly connected components are getting in stack.

Complexity
-------------
Kosaraju's algorithm runs in linear time i.e. O(V+E). But DFS Two Times (Transposed Graph and DFS for SCC)

Tarjan's Algorithm
---------------------------
Tarjan's Algorithm is based on the depth-first search algorithm only single time. 
The algorithm runs in linear time i.e. O(V+E).
Low-link array and discovery array, DFS

Concepts: 
    - discovery = {} is the discovery time of each nodes.
    - low = {} is the lowest discovery time of every nodes connected. So if we have a ancestor node connected (backedge)
        then we can assure back edge is there confirmed.
        
    - stack (trackStack) = {} - used to keep a track on nodes traversed in dfs and not backtracked.
        If on dfs if we came to a already visited node and not backtracked ie, still a backedge connection is there.
    - visited = {} is track of components visited.
        
Edge cases:
1. If backedge found a item in stack and already visted.Then low time of currentnode is updated with 
    min(vistitedNode[discovery], currentNode[low]).
2. On every backtrack after dfs (function), we update low value with min(vistitedNode[low], currentNode[low])..
3. Pop the current node from stack if discovery and low time are same.
4. If the low value and the disc value same it will be the head of an scc. So we will print whatever in stack.
 Since the stack is build if we found an item with same low and disc value, we pop the items from that index 
 so the items in stack after that is having same low value is scc.

Strongly Connected Components Applications
-----------------------------------
Vehicle routing applications
Maps
Model-checking in formal verification

"""

from collections import defaultdict

class GraphScc(object):
    def __init__(self, numofvertex):
        self.__numofvertex = numofvertex
        self.__graph = defaultdict(list)
        self.__time = 0
    
    def addEdge(self, start, destination):
        self.__graph[start].append(destination)
        
    def printScc(self):
        # print with list comprehension
        [print(key,':',item) for key, item in self.__graph.items()]
        
    def __sccUtility(self, vertex, discovery, lowLink, stackMemberVisit, currentStack: list):
        # discovery time set
        discovery[vertex] = self.__time
        lowLink[vertex] = self.__time
        self.__time += 1
        stackMemberVisit[vertex] = True
        currentStack.append(vertex)
        
        for toVertex in self.__graph[vertex]:
            # if not visited yet
            if  discovery[toVertex] == -1:
                self.__sccUtility(toVertex, discovery, lowLink, stackMemberVisit, currentStack)
                lowLink[vertex] = min(lowLink[vertex], lowLink[toVertex])
            #if the element visited
            elif stackMemberVisit[toVertex] == True:
                lowLink[vertex] = min(lowLink[vertex], discovery[toVertex])

        popStackItem = -1   
        if lowLink[vertex] == discovery[vertex]:
            while(popStackItem != vertex):
                popStackItem = currentStack.pop()
                print(popStackItem, end=' ')
                stackMemberVisit[popStackItem] = False
            print()
    
    
    # The Python lists and objects are passed by reference
    def getSCC(self):
        # discovery time of node
        discovery = [-1] * (self.__numofvertex)
        # low link array for low values of connected nodes
        lowLink = [-1] * (self.__numofvertex)
        # current stack member visited
        stackMemberVisit = [False] * (self.__numofvertex)
        # finally current stack
        currentStack = list()
        
        for vertex in range(self.__numofvertex):
            if discovery[vertex] == -1:
                self.__sccUtility(vertex, discovery, lowLink, stackMemberVisit, currentStack)
                
        
# Testing
graph = GraphScc(5)
graph.addEdge(0, 1)
graph.addEdge(1, 3)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
graph.addEdge(3, 4)
graph.addEdge(0, 3)

graph.getSCC()