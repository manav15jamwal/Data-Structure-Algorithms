# # LeetCode 2390 — Removing Stars From a String
# Goal : To remove last element when star appears
# Approach : Use stack list to append the elements in the array
# when star appears pop both star and its initial element
def remove_stars(array):
    stack = []
    for element in array:
        stack.append(element)
        if element == "*":
            for i in range(2):
                if stack:
                    stack.pop()
    return "".join(stack)

print(remove_stars("abc*d"))