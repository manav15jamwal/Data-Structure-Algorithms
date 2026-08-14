#Goal: You’re given an array of positive integers nums and a target target.Find Smallest window satisfying the condition

# Approach : Window expands until target hits or hits more than it 
# , then it checks window size and just updates the minimum count in loop
# left moves until window size is less than target

def minimum_subarray(array,target):

    left,right,count = 0,0,0
    minimum = float("inf")
    while right < len(array):
        count+=array[right]
        while count >= target:
            minimum = min(right-left+1,minimum)
            count-=array[left]
            left+=1
        right+=1
    if minimum == float("inf"):
        minimum=0
    return minimum

print(minimum_subarray([2,3,1,2,4,3],7))