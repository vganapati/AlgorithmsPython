#Heap Sort
#O(n lg n)

#max_heapify assumes that the heap obeys the max heap property EXCEPT for node
#we represent the heap with an appropriately ordered array
def max_heapify(list_1d,node_index):    
    child_left_index=node_index*2+1
    child_right_index=node_index*2+2
    
    node=list_1d[node_index]
    
    if len(list_1d)-1 < child_left_index: #if the node has no children, return
        return list_1d
    elif len(list_1d)-1 < child_right_index: #if the node has only 1 child
        child_left=list_1d[child_left_index]
        if node>=child_left:
            return list_1d
        else:
            list_1d[child_left_index]=node
            list_1d[node_index]=child_left
            return list_1d
    else:
        child_left=list_1d[child_left_index]
        child_right=list_1d[child_right_index]
        
        #swap node with the largest child, if child is larger   
        if (node>=child_left) and (node>=child_right):
            return list_1d
        else:
            if child_left>=child_right:
                #swap with left child
                list_1d[child_left_index]=node
                list_1d[node_index]=child_left
                node_index=child_left_index
            else:
                #swap with right child
                list_1d[child_right_index]=node
                list_1d[node_index]=child_right
                node_index=child_right_index
            #call max_heapify with the new list and new node index
            return max_heapify(list_1d,node_index)

def build_max_heap(list_1d):
    for index in range(len(list_1d)/2-1,-1,-1):
        max_heapify(list_1d,index)
    return list_1d

def heap_sort(list_1d):
    sorted_list=[]
    list_1d=build_max_heap(list_1d)
    
    while len(list_1d)>1:
        max_item=list_1d[0]
        #switch the last and the first item in the list
        list_1d[0]=list_1d[len(list_1d)-1]
        list_1d[len(list_1d)-1]=max_item
        #pop off max_item and add it to sorted_list
        sorted_list.insert(0,list_1d.pop())
        #max_heapify list_1d
        list_1d=max_heapify(list_1d,0)
    else:
        sorted_list.insert(0,list_1d.pop())
    return sorted_list

print heap_sort([2])
print heap_sort([-3,100,2])
print heap_sort([3,-2])
print heap_sort([2,3])
print heap_sort([1,3,2,3,4,5,6,899,7,2,3])
