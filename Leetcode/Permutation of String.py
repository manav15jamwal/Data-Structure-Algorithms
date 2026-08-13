# Goal: To check if any permutation of a string 1 exists in string 2
# Approach: Using hashmaps to count frequency of each character in string one
# Later on creating and updating hashmap of same size as of string one
# if both are equal return true else shift window through the string 2
# We donot compute all permutations because that will be a very computational costly and wrong Approach
# that is the reason of using hashmaps comparing the frequencies of characters ultimately confirms permutation
def permutation(str1,str2):
    if len(str1)>len(str2):
          return False
    left = 0
    right = 0
    hashmap1,hashmap2 = {},{}
    while right<len(str1) :
        # Below this code I will code Optimized alternative to it 
        if str1[right] not in hashmap1:
            hashmap1[str1[right]] = 1
        else:
            hashmap1[str1[right]]+=1
        if str2[right] not in hashmap2:
            hashmap2[str2[right]] = 1
        else:
            hashmap2[str2[right]]+=1
        right+=1
    if hashmap1==hashmap2:
                return True
    
    while right < len(str2):
        
        # Optimized loc 
        hashmap2[str2[right]] =  hashmap2.get(str2[right],0)+ 1
        
        if hashmap2[str2[left]] == 1:
                 hashmap2.pop(str2[left])
        else:
                 hashmap2[str2[left]] -= 1
        left+=1
        if hashmap1==hashmap2:
                    return True
        right+=1
    return False

print(permutation("abc","bcaccll"))
                 

    
 
        

