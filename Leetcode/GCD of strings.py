# Goal : To find whether both strings are made out of greatest single candidate String
# Approach : Use Gcd of both the strings to get number of candidate string length
# After finding the candidate key multiply candidate key by the floor of string//candidate key
# If both cadidate key * flooring == string That means strings are made out of that candidate key
from math import gcd
def is_candidate_key(string1,string2):
    g = gcd(len(string1),len(string2))
    candidate_key = string1[:g]
    # Checking both the strings are multiple of candidate key
    if (len(string1)//g)*candidate_key == string1 and (len(string2)//g)*candidate_key == string2:
        return candidate_key
    return None

string1 = "ababab"
string2 = "ababab"
print(is_candidate_key(string1,string2))
