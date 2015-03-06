#Breadth first search

#Representation of a graph as a nested list, e.g. [[2,3],[4,5],[6]]
#Each sub-list element with index i represents the node i 
#Each sub-list is a list of nodes reachable from i

#breadth_first finds the shortest path to all other vertices from the source_vertex
def breadth_first(graph,source_vertex):
    dist_list=[float("inf")]*len(graph) #dist_list keeps track of distance from source_vertex
    parent_list=[float("inf")]*len(graph) #parent_list keeps track of node's parent, 
                                          #inf means no parent
    color_list=["white"]*len(graph) #each node is colored white, gray, or black
                                    #when a node is discovered, it is turned gray
    dist_list[source_vertex]=0 #distance to itself is 0
    color_list[source_vertex]=["gray"]
    next_nodes=[source_vertex]
    while len(next_nodes)>0:
        node=next_nodes.pop()
        for child in graph[node]:
            if color_list[child]=="white":
                color_list[child]="gray"
                parent_list[child]=node
                dist_list[child]=dist_list[node]+1
                next_nodes.insert(0,child)
    return parent_list,dist_list

print breadth_first([[1],[0]],0)
print breadth_first([[1,4],[0,4,3,2],[1,3],[2,1,4],[0,1,3]],0)
print breadth_first([[1,4],[0,4,3,2],[1,3],[2,1,4],[0,1,3]],2)
print breadth_first([[1,3],[4],[5,4],[1],[3],[5]],0)
