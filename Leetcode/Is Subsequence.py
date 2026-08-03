# Goal to check if one candidate string is sub sequence of another string i.e Basically one string has all characters of other string
# Approach : Two pointer one points the candidate key ' character other searchs for it in entire string

def is_subsequence(str1,str2):
    fast,slow = 0,0
    # In case of "" empty string
    if len(str1) == 0:
        return True
    while fast < len(str2):
        if str1[slow] == str2[fast]:
            slow+=1
            if slow == len(str1):
                return True
        fast+=1
    return False
print(is_subsequence("abc","abnnnhc"))