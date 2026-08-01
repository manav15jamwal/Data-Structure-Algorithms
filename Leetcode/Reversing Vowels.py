# A String will be given need to pick out all the vowels in it and reverse order 
# and place back in the same position from where it was extracted
# eg: LEETCODE vowels = EEOE ,reverse = EOEE , result = LEOTCEDE
# Two pointer approach when left finds vowel and right two just swap them

def reverse_vowels(string1):
    # Used set for faster membership scanning than list
    vowels = set("aeiouAEIOU")
    # Used because Strings are immutable , Load on memory
    chars = list(string1)
    left = 0
    right = len(chars)-1
    while left < right:
        if chars[left] not in vowels:
            left+=1
            # To directly perform next iteration
            continue
        if chars[right] not in vowels:
            right-=1
            continue
        chars[left],chars[right] = chars[right],chars[left]
        left+=1
        right-=1
    return "".join(chars)

print(reverse_vowels("LeetCodingg"))