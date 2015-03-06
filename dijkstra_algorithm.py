#Dijkstra's algorithm
#finds the shortest path from a source vertex assuming nonnegative edge weights
#represent the edge weights with another nested list that mirrors graph representation

#the distance_list should be represented as a min priority heap for faster runtime
#in this algorithm, for simplicity we lookup the min of distance_list in O(n)
#with a min priority heap, this lookup would cost O(lg n)
def dijkstra(graph,weights,source_vertex):
    distance_list=[float("inf")]*len(graph) #change to min priority heap for faster runtime
    parent_list=[float("inf")]*len(graph)    
    distance_list[source_vertex]=0
    unfinished_vertices=[1]*len(graph)
    while sum(unfinished_vertices)>0:
        #extract unfinished_vertex with smallest distance
        vertex_i=[]
        dist_i=float("inf")
        for vertex,dist in enumerate(distance_list):
            if dist<dist_i and unfinished_vertices[vertex]:
                dist_i=dist
                vertex_i=vertex
        #remove vertex_i from the unfinished_vertices list
        unfinished_vertices[vertex_i]=0
        for index,adj_vertex in enumerate(graph[vertex_i]): #for each adjacent vertex to vertex_i
            edge_weight=weights[vertex_i][index]
            if distance_list[adj_vertex]>(distance_list[vertex_i]+edge_weight):
                distance_list[adj_vertex]=distance_list[vertex_i]+edge_weight
                parent_list[adj_vertex]=vertex_i    
    return distance_list,parent_list

#test
graph=[[1],[]]
weights=[[0.5],[]]
source_vertex=0

print dijkstra(graph,weights,source_vertex)

graph=[[1,4],[2,4],[3],[0,2],[3,2,1]]
weights=[[10,5],[1,2],[4],[7,6],[2,9,3]]
source_vertex=0

print dijkstra(graph,weights,source_vertex)
