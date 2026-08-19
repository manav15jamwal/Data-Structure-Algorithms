# Goal: If all elements in a list has different frequencies
# Approach : Use Hashmap to record the frequencies at last check if length of hashmap == len of set of values in hashmap

def unique_number_occurence(array):
    hashmap = {}
    for num in array:
        hashmap[num] = hashmap.get(num,0)+1
    return len(hashmap) == len(set(hashmap.values()))

print(unique_number_occurence([1,2,2,3,3]))

