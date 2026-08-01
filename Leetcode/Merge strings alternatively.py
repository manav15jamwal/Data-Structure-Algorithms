#Leetcode 1768

# Merge Strings Alternatively
# one letter from word1 other from word2 in this order if either of string is long just concatenate the rest of string.
# Approach:
# To create a list which will hold the result by transversing through both the strings in alternate order. 
# Make sure to implement a length check before proceeding with the concatenation.
# Using list rather than string variable because of strings immutable nature i.e. If we 
# use string variable in loop , it creates new string at each iteration increasing the
# Space Complexity

def merge_strings(word1,word2):
    result = []
    i = 0
    while len(word1)>i or len(word2)>i:
        if i < len(word1):
            result.append(word1[i])
        
        if i < len(word2):
            result.append(word2[i])
        i += 1

    return "".join(result)

print(merge_strings("abc","pqrst"))