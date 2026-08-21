def compress(chars):
        seen = set()
        result = []
        count=1
        index = 0
        while index < len(chars):
            
            if chars[index] in seen:
                count+=1
          
                if index == len(chars)-1:
                    if count > 1:
                        if count<10:
                            result.append(str(count))
                            count = 1
                        elif count >= 10:
                            i = 0
                            while count >0:
                                count-=10
                                i+=1
                                result.append(str(i))
                            count = 1
                        seen = seen.clear()
            elif chars[index] not in seen:
                if count > 1:
                    if count<10:
                        result.append(str(count))
                        count = 1
                    elif count >= 10:
                        i = 0
                        while count > 0:
                            count-=10
                            i+=1
                            result.append(str(i))
                            seen = seen.clear()
                        count+=1
                result.append(chars[index])
                seen.add(chars[index])
            index+=1

        return result

print(compress(["a","b","c","d","e","f","g","g","g","g","g","g","g","g","g","g","g","g","a","b","c"]))