#longest common sub-string
#find the longest common sub-string in 2 strings, not necessarily consecutive 
#dynamic programming, bottom-up
#O(length(string1)*length(string2))

#keeps track of the longest substring length for all the sub-problems, substring_value
#keeps track of a table that contains pointers to the next smaller substring, substring_pointer
#in string_pointer, 0 is north arrow, 1 is west arrow, 2 is northwest arrow
def lcss(string_x,string_y):
    substring_value=[[0]*(len(string_y)+1) for i in range(len(string_x)+1)] 
    substring_pointer=[[0]*(len(string_y)) for i in range(len(string_x))]
    for index_x in range(0,len(string_x)):
        for index_y in range(0,len(string_y)):
            if string_x[index_x]==string_y[index_y]:
                substring_value[index_x+1][index_y+1]=substring_value[index_x][index_y]+1
                substring_pointer[index_x][index_y]=2
            elif substring_value[index_x][index_y+1]>=substring_value[index_x+1][index_y]:
                substring_value[index_x+1][index_y+1]=substring_value[index_x][index_y+1]
                substring_pointer[index_x][index_y]=0
            else:
                substring_value[index_x+1][index_y+1]=substring_value[index_x+1][index_y]
                substring_pointer[index_x][index_y]=1
    return substring_value,substring_pointer

#prints the substring
def print_lcss(substring_value,substring_pointer,string_x,string_y):
    current_x=len(substring_value)-1
    current_y=len(substring_value[0])-1
    substring=[]
    current_value=float("Inf")
    while current_x>0 and current_y>0:
        current_value=substring_value[current_x][current_y]
        current_pointer=substring_pointer[current_x-1][current_y-1]
        if current_pointer==0:
            current_x=current_x-1
        elif current_pointer==1:
            current_y=current_y-1
        elif current_pointer==2:
            substring.insert(0,string_x[current_x-1])
            current_x=current_x-1
            current_y=current_y-1
    return substring

string_x='abc'
string_y='abc'
(substring_value,substring_pointer)=lcss(string_x,string_y)
print print_lcss(substring_value,substring_pointer,string_x,string_y)

string_x='w'
string_y='w'
(substring_value,substring_pointer)=lcss(string_x,string_y)
print print_lcss(substring_value,substring_pointer,string_x,string_y)

string_x='abcbdab'
string_y='bdcaba'
(substring_value,substring_pointer)=lcss(string_x,string_y)
print print_lcss(substring_value,substring_pointer,string_x,string_y)
