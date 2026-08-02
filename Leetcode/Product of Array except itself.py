# Problem: To find product of every element except itself 
# Approach: We need two things:
#                             1. Prefix product
#                             2. Postfix product
# Create an array of one with length of array
# Initialize product variable which will store prefix product or postfix product 

def product_except_itself(array):
    result = [1]*len(array)
    product = 1
    i = 0
    # Finding Prefix of each element
    while i < len(array):
        
            result[i] = product
            product*=array[i]
            i+=1
    # Re-initializing variables for postfix solution * Prefix solution
    product = 1 
    i -= 1
    while i >= 0:
            
                result[i] *= product
                product*=array[i]
                i-=1
    
    return(result)
        
array = [1,2,3,4]
print(product_except_itself(array))