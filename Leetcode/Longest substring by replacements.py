# Goal : To return longest possible substring by replacing atmost in Upper case letters
# Approach : Use hashmap 
# keep check on most frequent character,
# longest is max of size of window - most frequent > = k,
# shrink the window if k < size_of_window - most frequent

def longest_with_replacement(string , k):
    seen = {}
    left, right = 0,0
    longest = 0

    while right<len(string):
        if string[right] not in seen:
            seen[string[right]]=1
        else:
            seen[string[right]]+=1
        frequent = max(seen.values())
        while k < (right-left+1)-frequent:
            seen[string[left]]-=1
            left+=1
        longest = max(longest,right-left+1)
        right+=1
    return longest
print(longest_with_replacement("AABABB",1))