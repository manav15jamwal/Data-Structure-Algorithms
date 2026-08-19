# Leetcode 2215
# Goal : To return arrays , array1 without elements in array 2 andarray2 without elements of array1
# Approach : Convert them into sets as it needs distinct values, take out the differences , convert it back to list and  return
def difference_of_arrays(array1,array2):
    set1 = set(array1)
    set2 = set(array2)
    a1 = list((set1-set2))
    a2 = list((set2-set1))
    return a1,a2

print(difference_of_arrays([1,2,2,3],[2,4,4,5]))