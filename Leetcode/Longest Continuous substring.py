# Goal : A string is given "aaabseee" to find length of "abse" i.e Continuous unique substring
# Approach : Using two pointers (sliding window) and set 
# when right pointer expands it maintains a set ,
# if string[right] is in set then remove all the elements by incrementing left untill string[right] is removed
#     Passing through the string make sure track longest string and return it in last

def longest_continuous_substring(string):
    left , right = 0,0
    seen = set()
    longest = 0
    while right < len(string):
    #     Can use while string[right] in seen:
    #         seen.remove(string[left])
    #                     left+=1     
        
        if string[right] in seen: 
            seen.remove(string[left])
            left+=1
        else:
            seen.add(string[right])
            longest = max(longest,right-left+1)
            right+=1
    return longest
        
print(longest_continuous_substring("abba"))     