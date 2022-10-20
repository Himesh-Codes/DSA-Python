"""
Articulation Points (or Cut Vertices) in a Graph

Given a grapth, the task is to find the articulation points in the given graph.

Note: A vertex in an undirected connected graph is an articulation point (or cut vertex) if removing 
it (and edges through it) disconnects the graph. Articulation points represent vulnerabilities in a connected network 
– single points whose failure would split the network into 2 or more components. 
They are useful for designing reliable networks.
Eg: Input = [[1,2], [2,4], [4,0], [2,3], [3,5]]
Output = 
Bruteforce Approach
-----------------
A simple approach is to one by one remove all vertices and see if removal of a vertex causes disconnected graph.
We can see the graph is connected using DFS traversal.
Time Complexity: O(V*(V+E)) 

Solution
-----------
DFS Tree Traversal (Tarjan's Algorithm)

Concepts: 
    - discovery = {} is the discovery time of each nodes.
    - low = {} is the lowest discovery time of every nodes connected. So if we have a ancestor node connected (backedge)
        then we can assure back edge is there confirmed.
    - parent = {} the parent of each node is found.
    - AP = {} the articulation point items
    - childcount = {}  the number of child of each node.
Solution
----------
1. Do a DFS on the graph, with updating disc, low, parent, childcount, AP.
2. We updates the AP if found the item is an AP, parent value on the traversal (don't update in respsect to visited node).
3. Child count is only for unvisited child nodes, becuase visited child node means it have other parent.

Edge Cases
-----------
1. If on DFS traversal a visited node revisited again, then low[cur] = min(disc[toVertex], low[cur]). ie, the low time
    is updated on these adjacent current in comparison with child node.
2. On backtrack we will be updating the low[cur] = min(low[child], low[cur]). Becuase need to check a loop is there with
    less low time to reach current node.
3. On every backtrack of DFS, Condition to determine is AP is if (child) low[i+1] >= disc[i] (current/parent node) 
    && parent != 1. 
    (Becuase on every backtrack we can assure that its child adjacent element is not having a link to its parent's parent
    , So we can make it AP).
4. If parent == -1 we need to assure it is having a child value >= 2.(Note child is only the count of unvisited children).

"""

class Graph:
    def __init__(self):
        self.graphs = {}
        self.time = 0
        
    def getArticulationPoints(self, V, adj):
        
        def dfs(currentVertex, parentVertex):
            if currentVertex is not None:
                discovery[currentVertex] = self.time
                low[currentVertex] = self.time
                if parentVertex is not None: parent[currentVertex] = parentVertex
                self.time += 1
                
                for child in self.graphs[currentVertex]:
                    # visited node condition
                    if child in discovery and discovery[child] != -1:
                        low[currentVertex] = min(low[currentVertex], discovery[child])
                    else:
                        # count of unvisited children
                        childCount[currentVertex] += 1
                        dfs(child, currentVertex)
                        # check the AP condition, check on low of child confirm no back link exists.
                        if low[child] >= discovery[currentVertex] and parent[currentVertex] != -1: 
                            AP[currentVertex] = True
                        low[currentVertex] = min(low[currentVertex], low[child])
                # check for root element is AP
                if parent[currentVertex] == -1 and childCount[currentVertex] >= 2:
                    AP[currentVertex] = True
                
            
        discovery = {}
        low = {}
        parent = {}
        AP = {}
        childCount = {}
        head = None
        # initialise vertex values
        for vertex, toVertex in adj:
            head = vertex if head is None else head
            discovery[vertex] = discovery[toVertex] = -1
            low[vertex] = low[toVertex] = -1
            parent[vertex] = parent[toVertex] = -1
            AP[vertex] = AP[toVertex] = False
            childCount[vertex] = childCount[toVertex] = 0
            if vertex in self.graphs:
                self.graphs[vertex].append(toVertex)  
            else:
                self.graphs[vertex] = [toVertex]
            if toVertex in self.graphs:
                    self.graphs[toVertex].append(vertex)  
            else:
                self.graphs[toVertex] = [vertex]
        dfs(head, None)
        points = []
        for index, value in AP.items():
            if value == True:
                points.append(index)
        return points if len(points) > 0 else [-1]
        

# Testing

vertex = [1,2,3,4,5]
adjacentList = [[1,2], [2,4], [4,1], [2,3], [3,5]]
graph = Graph()
print(graph.getArticulationPoints(vertex, adjacentList))
vertex = [0,1,2,3,4,]
adjacentList = [[0,1], [1,4], [4,2], [4,3], [2,3]]
print(graph.getArticulationPoints(vertex, adjacentList))