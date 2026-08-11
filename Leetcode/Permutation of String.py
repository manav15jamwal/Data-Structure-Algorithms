def permutation(str1,str2):
    left = 0
    right = 0
    hashmap1,hashmap2 = {},{}
    while right<len(str1) :
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
                 

    
 
        

