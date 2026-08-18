# Goal : To find the leftmost index of array whose sum to right == sum of right
# Approach : Get a variable storing sum of array, traverse the array totalling the left sum 
# check if  leftsum = right -leftsum

def pivot(array):
    right_sum = sum(array)
    left_sum,left = 0,0
    while left < len(array):
        if left_sum == right_sum-left_sum-array[left]: 
            print(f"right sum:{right_sum-left_sum-array[left]},left sum:{left_sum},num:{array[left]}")
            return left
        left_sum += array[left]
        left+=1
    return 0

print(pivot([1, 7, 3, 6, 5, 6]))
        