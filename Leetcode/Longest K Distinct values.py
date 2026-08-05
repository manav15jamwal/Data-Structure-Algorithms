# Goal : To find maximum length od substring that has k number of characters
# Approach : We will use Hashmap here not a set because we need to track count of characters
# e.g : "eeeebccccaaaaaa" , k = 3, longest substring is : bcccaaaaaa
# now to reach at b we must know how many left to move to eliminate a character 
# if set used it will eliminate first e and then declare there is no e in the string left

def max_k_distinct(string,k):
    seen = {}
    left,right = 0,0
    longest = 0
    while right < len(string):
        if string[right] not in seen:
            seen[string[right]] = 1
        else:
            seen[string[right]]+=1
        while len(seen) > k:
            if seen[string[left]] == 1:
                seen.pop(string[left])
            else:
                seen[string[left]]-=1
            left+=1
        longest = max(longest,right-left+1)
        right+=1
    return longest
print(max_k_distinct("eeeebccccaaaaaa",3))
