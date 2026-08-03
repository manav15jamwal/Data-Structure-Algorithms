# # Goal : To check if increasing triplet exists in the array. Remember i>j>k th positions of array
# i.e large values to be in the right side of array
# # Do not think of it as a sliding window : Its simpler than it
# # Its GREEDY Approach
# # Approach : use Incrementing loop update first smallest and second smallest number while iterating
# if number exists larger than both first smallest and second smallest just return True


def increasing_triplet(array):
    first_small = float("inf")
    second_small = float("inf")
    for num in array:
        if num <=first_small:
            first_small = num
        elif num <= second_small:
            second_small = num
        else:
            return True
    return False
print(increasing_triplet([3,2,9,10]))