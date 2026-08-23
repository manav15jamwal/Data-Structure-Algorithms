# Goal : To compress the string if character repeats more than one and less than 10 , write it as "a","9" , 
# but  if exceeds 10; "a","1","2", if it does not repeat simply write a
# Approach: Use a set to check if same character is repeating or another:
# when character changes append the count in result
# in case of repeating char till end of the string use elif condition for incrementing cound and adding it to result
# in else block increment the count; at last join it as string and return the length
def compress(chars):
        seen = set()
        result = []
        count=1
        index = 0
        while index < len(chars):
            if chars[index] not in seen:
                  if count > 1:
                        result.append(str(count))
                        count = 1
                  seen.clear()     
                  result.append(chars[index])
                  seen.add(chars[index])
            elif index == len(chars)-1:
                  count+=1
                  result.append(str(count))
            else:
                  count+=1
            index+=1
        result = "".join(result)

        print(list(result))
        return len(result)

print(compress(["a","b","c","d","e","f","g","g","g","g","g","g","g","g","g","g","g","g","a","b","c"]))