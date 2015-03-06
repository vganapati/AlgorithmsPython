#Cut Rod 
#Dynamic Programming, bottom-up

#We need to figure out how to optimally cut a rod for maximum value
#Each length of the rod corresponds to a selling value, given by the list prices
#prices[0] is the value of a rod of 0 unit, prices[1] for 1 unit, etc.
def cut_rod(total_length,prices):
    prices[0]=0 #Force prices[0] to be 0
    optimal_values=[0]*(total_length+1) #optimal_values hold the optimal price for length index
    for index in range(1,total_length+1):
        value=float("-inf")
        for index2 in range(1,index+1):
            value=max(value,prices[index2]+optimal_values[index-index2])
        optimal_values[index]=value
    return optimal_values[total_length]

print cut_rod(2,[0,10,100,2])
print cut_rod(3,[0,10,100,2])
print cut_rod(6,[0,1,5,8,9,10,17,17,20,24,30])
