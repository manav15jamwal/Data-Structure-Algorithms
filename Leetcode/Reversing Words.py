def reverse_words(string1):
    result = []
    left,right = 0,0
    while left < len(string1):
        if string1[left] == " ":
           left+=1
           right+=1
           continue
        # If sentence didnt end with space right will move out first condition prevents exceeding index 
        if right<len(string1) and string1[right] !=" " :
            right+=1
            continue
        result.append(string1[left:right])
        left = right
    result.reverse()
    return " ".join(result)
print(reverse_words("My name is Manav"))

        
        