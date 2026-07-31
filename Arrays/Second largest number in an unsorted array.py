# To find The Second Largest number in an unsorted array
# Using previous approach but using two variables to hold largest and second largest both

def second_largest_number(arr):

    if arr:
        i = 0
        largest = arr[i]
        second_largest = float("-inf")
        while len(arr) > i:
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
    #Make sure you have arr[i]!=largest condition else in case of duplicates you will get largest as second largest
            elif arr[i] > second_largest and arr[i]!=largest:
                second_largest = arr[i]
            i+=1
    #Do not forget to set second largest to -1 in case of singular arrays make sure it returns -1
        if second_largest == float("-inf"):
            return -1
        return second_largest
    return None
print(second_largest_number([10,20,20,15]))
print(second_largest_number([20,20]))


        

    