# Goal : Asteroids are given in order , size is represented by the number and its sign represents its direction if size of asteroid is big and opposite
# it pops the smaller asteroids in collection

def ast_collision(array):
    stack = []
    for ast in array:
      
        while stack and ast<0 and stack[-1] > 0:
                if -ast > stack[-1]:
                    stack.pop()
                    continue
                elif -ast == stack[-1]:
                    stack.pop()
                break
        else:
            stack.append(ast)
    return stack
print(ast_collision([10,5,-5,5,20]))