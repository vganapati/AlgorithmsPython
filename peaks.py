
#1D Peak Finding Algorithm
#The function returns any peak in a 1D list
#A peak is defined as a value that is greater than or equal to its neighbors
#It is assumed that values of -Inf border the ends of the list

#O(n) time
def find_1d_peaks(list_1d): #returns the value of any peak
    if len(list_1d)==1:
        return list_1d[0]
    for index,value in enumerate(list_1d): #go through list, and return if value is a peak
        if index==0: #first item in list
            if value>=list_1d[1]:
                return value
        elif index==len(list_1d)-1: #last item in list
            if value>=list_1d[len(list_1d)-2]:
                return value
        else: #middle item in list
            if value>=list_1d[index-1] and value>=list_1d[index+1]:
                return value

#O(lg n) time

def find_1d_peaks_faster(list_1d):
    if len(list_1d)==1: #if there is 1 item in the list, that item is the peak
        return list_1d[0]
    elif len(list_1d)==2: #if there are 2 items in the list, the larger item is the peak
        if list_1d[0]>list_1d[1]: 
            return list_1d[0]
        else:
            return list_1d[1]
    else: #if there are more than 2 items
        #run the algorithm recursively on the sub-list in the increasing direction
        #return the middle item if it is a peak
        if list_1d[len(list_1d)/2]>=list_1d[len(list_1d)/2-1]         and list_1d[len(list_1d)/2]>=list_1d[len(list_1d)/2+1]: 
            return list_1d[len(list_1d)/2]
        elif list_1d[len(list_1d)/2]<list_1d[len(list_1d)/2-1]:
            return find_1d_peaks_faster(list_1d[0:len(list_1d)/2])
        else:
            return find_1d_peaks_faster(list_1d[len(list_1d)/2+1:])
      
#test

print "O(n)"
print find_1d_peaks([1])
print find_1d_peaks([1,2])
print find_1d_peaks([7,1,3,2,7,2])
print find_1d_peaks([1,2,3,7,7,1,3,2,7,2])
print find_1d_peaks([7,1,1,8,1,1])

print "O(lg n)"
print find_1d_peaks_faster([1])
print find_1d_peaks_faster([1,2])
print find_1d_peaks_faster([7,1,3,2,7,2])
print find_1d_peaks_faster([1,2,3,7,7,1,3,2,7,2])
print find_1d_peaks_faster([7,1,1,8,1,1]) #does not find the same peak as find_1d_peaks
