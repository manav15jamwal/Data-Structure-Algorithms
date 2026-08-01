# A Flowerbed is represented by an array
# Plots are indexes in array and 0 means empty and 1 means filled
# Rule: No adjacent plots can be filled
# Problem : Given n integer flowers can be filled while following the rules

def flowerbed(arr,n):
    i = 0
    while i < len(arr):
       
        if arr[i] == 0 and (i==0 or arr[i-1] == 0) and ( i==len(arr)-1 or arr[i+1] == 0  ):
            arr[i] = 1
            n-=1
            # Skips to next to next to complete loop fast following the rule
            i+=2
        else:
            i+=1
    if n == 0:
            return True
    return False

arr = [1,0,0,0,0]
n = 2
print(flowerbed(arr,n))