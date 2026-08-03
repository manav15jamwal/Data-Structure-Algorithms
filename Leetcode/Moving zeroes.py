# Goal : To move zeroes to one side without changing the order of non zero elements
# Approach two pointers, left or slow pointer tracking the non zeroes and right tracking  zeroes

def move_zeroes(array):
    left = 0
    right = 0

    while right < len(array):
        # Do not overcomplicate situation by writing number of statements.
        # Just swap and increment left when right points to non zeroes:
        # No special handling for left pointer needed here
        if array[right] != 0:
            array[left],array[right] = array[right],array[left]
            left+=1
        right+=1
    return array
    

print(move_zeroes([1,0,2,0,3]))

