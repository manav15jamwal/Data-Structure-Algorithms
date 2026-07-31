# Largest Number in an unsorted Array
# Do not sort the array it will increase the time complexity
# CUE: one comparison at a time assume the first element as largest, compare with rest of elements one by one.

def largest_number(arr):
    i = 0
    largest = arr[i]
    while i<len(arr):

        if largest < arr[i]:
            largest = arr[i]
        i += 1
    return largest

arr1 = [10,12,0,2]
arr2 = [-2,-23,-1]
print(largest_number(arr1))
print(largest_number(arr2))