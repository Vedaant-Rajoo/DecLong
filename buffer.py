n,m=map(int,input().split())
from collections import defaultdict 
  
# function for adding edge to graph 
graph = defaultdict(list) 
def addEdge(graph,u,v): 
    graph[u].append(v) 
  
# definition of function 
def generate_edges(graph): 
    edges = [] 
  
    # for each node in graph 
    for node in graph: 
          
        # for each neighbour node of a single node 
        for neighbour in graph[node]: 
              
            # if edge exists then append 
            edges.append((node, neighbour)) 
    return edges 