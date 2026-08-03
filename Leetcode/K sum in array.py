# Goal: To find number of pairs in an array which sums up to k integer
# Approach: Sort array first so that small numbers come to the left and larger to the right
# Take two pointers pointing at the two different ends
# Loop it till left one is smaller than right
# if total of two pointed values is larger than k , decrement right
# if total is smaller than k increment left because its a sorted array
def ksum(array,k):
    left = 0
    right = len(array)-1
    cases = 0
    array.sort()
    while left<right:
       total = array[left]+ array[right]
       if total == k:
            cases+=1
            left+=1
            right-=1
       elif total > k:
           right-=1                       
       else:
            left+=1
    return cases


print(ksum([1,2,3,4],5))