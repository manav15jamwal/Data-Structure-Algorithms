# Given an array of positive integers nums and an integer k, return the number of contiguous subarrays whose product is strictly less than k
# Approach : Use a window which expands until its product is less than k, increase the count with window size
# while product exceeds k shrink the window,increase count again in order to not miss the corrected subarray

def subarray_product_less_than_k(array,k):
    count,left,right = 0,0,0
    product = 1
    while right < len(array):
        product *= array[right]
        if product < k:
            count+=right-left+1
        else:
            while product>=k:
                product /= array[left]
                left+=1
            # This prevents missing a subarray while decreasing the product
            if product != 0:
                count+=right-left+1
        right+=1
    return count
print(subarray_product_less_than_k([10, 5, 2, 6],k = 100))