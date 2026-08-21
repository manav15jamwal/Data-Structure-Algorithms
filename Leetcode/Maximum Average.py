# # LeetCode 643
# Goal : To find a subarray of k length with highest average in the array
# Approach : Use sliding window concept left pointer tracks the initial element, right moves till k length
# When window reaches k limit, increment left pointer
# Update average at each k length iteration and return maximum avg 

def max_avg(array,k):
    avg = float("-inf")
    total = 0
    left , right =0,0
    while right < len(array):
        total += array[right]
        if right - left == k-1:
# Other way:
#         as k keeps constant
#         just track total,
#         Find max total ; return max total/k 
            avg = max(avg,total/k)
            total-=array[left]
            left+=1
        right+=1
    return avg
print(max_avg([9,7,3,5,6,2,0,8,1,9],6))