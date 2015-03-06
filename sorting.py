#Insertion Sort
#O(n^2)

def insertion_sort(list_1d):
    for index,item in enumerate(list_1d):
        for i in range(index-1,-1,-1): #check that all values below item are smaller
            if list_1d[i+1]<list_1d[i]:
                list_1d[i+1]=list_1d[i] #swap positions
                list_1d[i]=item
            else:
                break
    return list_1d   

#Merge Sort      
#O(n lg n)

def merge_sort(list_1d):
    if len(list_1d)==1: #already sorted
        return list_1d
    else: 
        #split input into 2 lists
        #merge_sort each of the 2 lists
        sub_list1=merge_sort(list_1d[:len(list_1d)/2])
        sub_list2=merge_sort(list_1d[len(list_1d)/2:])
        #merge the results of the 2 merge_sorts
        count=0
        for item2 in sub_list2:
            #insert item into proper position in list_1d
            for number,item in enumerate(sub_list1[count:]):
                if item2<item:
                    sub_list1.insert(count+number,item2)
                    count+=number+1
                    break
            else:
                sub_list1.append(item2)
                count+=number+2
        return sub_list1

#test
print "Insertion Sort, O(n^2)"
print insertion_sort([5])
print insertion_sort([5,2])
print insertion_sort([5,2,3,1,3,7,1,2,10,1,3,2,2,5])

print "Merge Sort, O(n lg n)"
print merge_sort([5])
print merge_sort([5,2])
print merge_sort([5,2,3,1,3,7,1,2,10,1,3,2,2,5])
