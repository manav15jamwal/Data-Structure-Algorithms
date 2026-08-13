# Goal : With a given k size of window , return the maximun number of vowels in full string
# Approach : Create two pointers left and right , and a set containing all vowels
# while window size reaches size k,
# keep count of vowels
# move left pointer when size exceeds k , if leftmost item is a vowel just decrement count
# return maximum out of whole traversal

def max_vovels(string,k):
    max_count,count = 0,0
    vowels = {"a","i","o","u","e"}
    left = 0
    for right in range(len(string)):
        if string[right] in vowels:
            count+=1
        if right-left+1 > k:
            if string[left] in vowels:
                count-=1
            left+=1
        max_count = max(count,max_count)
    return max_count
        

print(max_vovels("stiingi",3))