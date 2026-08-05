# Goal : Given a binary array and k, we can turn zero into 1 for k times only
#     need to return longest contiguous length of ones
# Approach : Initialize two pointers left and right
#  right will iterate through and check if number is 0 or 1 , if 0 increment zero_count
#  if zero_count > k: move left pointer and decrement zero count till left finds zero to pop out.

def max_consecuitive(array,k):
    left , right = 0,0
    zero_count = 0
    longest = 0
    while right<len(array):
        if array[right]==0:
            zero_count+=1
# Looping here doesnt change it to O(n^2) as it only go for less iterations in a specific case only
        while zero_count > k:
            
            if array[left]==0:
                zero_count -=1
            left+=1
        longest = max(longest,right-left+1)
        right+=1
    return longest
print(max_consecuitive([1,1,0],0))
