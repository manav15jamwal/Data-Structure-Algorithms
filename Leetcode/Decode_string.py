# Goal: Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
#  Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
#  Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat number
# s, k. For example, there will not be input like 3a or 2[4].
# Approach : Keep a string reserved , look for a digit take it as a multiplier, and append that tuple/list of both in a stack
#     while iterating it encounters "[" starts tracking the substring and when encountering "]" end just
#     fetch last reserved string and multiplier, multiply the substring and concatenate it into the reserved string

def decode_string(string):
    stack = []
    sub_str = ""
    multiplier = 0
    for char in string:
        if char.isdigit():
            multiplier = multiplier*10 + int(char)
        elif char == "[":
            stack.append((sub_str,multiplier))
            multiplier = 0
            sub_str = ""
        elif char == "]":
            res_str,res_mult = stack.pop()
            sub_str = res_str+res_mult*sub_str
        else:
            sub_str += char
    return sub_str
print(decode_string("3[abc4[d]]"))


