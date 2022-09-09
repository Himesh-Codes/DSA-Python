"""

Bellman Ford algorithm used to find Single Source Shortest Path from a source node to any other nodes in a Graph.
The Graph here contains the weights for each edges where the nodes are connected. 

***** Application Example *****
Used Modified Bellman Ford Algorithm with BFS
Cheapest Flight Within Atmost K Stops : From Source To Destination

Complexity
-------------
O(EV) is the complexity.
So the better is Dijikstra's algorithms, with complexity O((E+V) log(V))
Only advantage over dijikstra's algorithm is when graph have negative edges.

Applications
-------------
Short Path and Negative cycle ( eg: financial applications)

Algorithm Steps
----------------
E : No: of Edges, V : No: of Vertices, S : Id of starting node, D : Array of best distance from S to each nodes.
1. Every entry in Distance (D) array as + infinity. Since all nodes distances are unknown
2. Set D[S] = 0
3. Relax each edge V-1 times: (We run the V-1 loop, loop in all edges of graph, all update the shortest distance path, 
                            if D[edge.from] + edge.cost <  D[edge.to], update D[edge.to] = D[edge.from] + edge.cost)
4. To find negative cycle we runs the algorithm second time: 
                (  if D[edge.from] + edge.cost <  D[edge.to], update D[edge.to] = - infinity)
                
Psuedo Code
----------------
function bellmanFord(G, S)
  for each vertex V in G
    distance[V] <- infinite
      previous[V] <- NULL
  distance[S] <- 0

  for each vertex V in G				
    for each edge (U,V) in G
      tempDistance <- distance[U] + edge_weight(U, V)
      if tempDistance < distance[V]
        distance[V] <- tempDistance
        previous[V] <- U

  for each edge (U,V) in G
    If distance[U] + edge_weight(U, V) < distance[V}
      Error: Negative Cycle Exists

  return distance[], previous[]

"""

class ChartFlight(object):
    def __init__(self, **kwargs):
        self.__flights: list[list[int]] = kwargs['flights'] if 'flights' in kwargs else []
        self.__totalnodes = kwargs['numofcities'] if 'numofcities' in kwargs else 0
        
    def findCheapestFlight(self, source: int, destination: int, stops: int):
        priceArray = [float('inf')] * self.__totalnodes
        priceArray[source] = 0
        
        for iteration in range(stops + 1):
            # copy the array
            temporaryPrices = priceArray.copy()
            for sourcePlace, destinationPlace, cost in self.__flights:
                if priceArray[sourcePlace] == float('inf'):
                    continue
                if temporaryPrices[destinationPlace] > priceArray[sourcePlace] + cost:
                    temporaryPrices[destinationPlace] = priceArray[sourcePlace] + cost
            priceArray = temporaryPrices
        return priceArray, priceArray[destination]
    
# Testing
flights = [[0,1,100], [0,2,500], [1,2,100]]
flightCalculator = ChartFlight(flights= flights, numofcities = 3)
priceCharts, travelPrice = flightCalculator.findCheapestFlight(0,2, 1)
print("The Price Chart:", priceCharts)
print("Total Travel Price", travelPrice)