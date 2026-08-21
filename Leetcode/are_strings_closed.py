# Leetcode : 1675
# Goal : To find if strings are closes that means two strings share same characters it might swapped
# e.g : "abc" and "bac"  and
# it can swap the frequencies as well e.g : "aabbb" and "aaabb" are closed

# Approach:
# We know two find the permutational relation hashmaps are optimised approach.
# To check the  frequencies are equal, just sort the order of its values and return the answer:
def are_closed(string1,string2):
    if len(string1)!=len(string2):
        return False
    hash1 = {}
    hash2 = {}
    for i in range(len(string1)):
        hash1[string1[i]] = hash1.get(string1,0)+1
        hash2[string2[i]] = hash1.get(string2,0)+1

    if hash1.keys() == hash2.keys():
        return sorted(hash1.values()) == sorted(hash2.values())
    return False

print(are_closed("aab","bba"))
                
