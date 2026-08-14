# LeetCode 904: 
# Goal:
# You have an array where each number represents a type of fruit.You have two baskets, 
# and each basket can hold only one type of fruit.You want to collect the maximum number of consecutive fruits 
# while having at most 2 distinct types.
# Approach: Use hashmap to record frequency plus types of fruit as the size exceeds two pop the left until its completely removed from hashmap
# track maximum

def fruits_into_basket(array):
    maximum,left,right = 0,0,0
    seen = {}
    while right < len(array):
        seen[array[right]] = seen.get(array[right],0)+1
        if len(seen) > 2:
            if seen[array[left]]>1:
                seen[array[left]]-=1
            else:
                seen.pop(array[left])
            left+=1
        maximum = max(maximum,sum(seen.values()))
        right+=1
        print(seen)
    return maximum

print(fruits_into_basket([1,2,1,2,3]))