# In this problem we will be given candies array which represents number of candies to particular
# i th candidate 
# Goal : To find if extra candies n given to each child which children will have maximum number of 
# cadies with them

# Approach :
# Find max number of candies 
# while iterating through the array just add and check if its more or equal than max
# if yes append the boolean answer True or False in result list.

def max_candies(arr,extra_candies):
    maximum = max(arr)
    i = 0
    result = []
    for candy in arr:
        if candy+extra_candies >= maximum:
            result.append(True)
        else:
             result.append(False)
        i += 1
    return result

arr = [4,2,2,1]
extra_candies = 2
print(max_candies(arr,extra_candies))