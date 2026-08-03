# Goal : To find optimal heights of container to get most of water
# Approach : Two pointers one at beginning one at the end
# Both shrinks inwards, shorter wall side gets shrinked
# Area is calculate by min of both height multiplied by the length of index

def container_with_most_water(array):
    beg = 0
    end = len(array)-1 
    area = 0

    while beg!=end:

        area = max(area,(min(array[beg],array[end])*(end-beg)))
        if array[beg] > array[end]:
            end-=1
        else:
            beg+=1
    return area

print(container_with_most_water([1,8,6,2,5,4,8,3,7]))