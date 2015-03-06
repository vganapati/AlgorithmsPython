#Counting Sort
#O(n) when upper_bound matches the largest value of the input list
#works for non-negative integers

def counting_sort(list_1d,upper_bound): #upper_bound must be greater than the 
                                        #largest element in list_1d
    temp_list=[0]*(upper_bound+1)
    sorted_list=[0]*len(list_1d)
    sorted_list_index=[0]*len(list_1d)
    
    for number in list_1d:
        temp_list[number]=temp_list[number]+1

    #Now for each index in temp_list, we have the number of corresponding values in list_1d
    for index in range(1,len(temp_list)):
        temp_list[index]=temp_list[index]+temp_list[index-1]
    #Now temp_list contains the number of values equal and less than the index

    for index in range(len(list_1d)-1,-1,-1):
        sorted_list[temp_list[list_1d[index]]-1]=list_1d[index]
        sorted_list_index[temp_list[list_1d[index]]-1]=index
        temp_list[list_1d[index]]=temp_list[list_1d[index]]-1
    return sorted_list,sorted_list_index

#test
print counting_sort([2],3)
print counting_sort([3,100,2],100)
print counting_sort([3,2],100)
print counting_sort([2,3],100)
print counting_sort([1,3,2,3,4,5,6,7,0,2,3,99,50,10],100)
