stack = []



stack.append('A')
stack.append('B')
stack.append('C')
print('Stack', stack)



topElement = stack[-1]
print("peek: ", topElement)


poppedElement = stack.pop()
print('Pop:', poppedElement)

print("Stack after pop", stack)

isEmpty = not bool(stack)
print("isEmpty", isEmpty)



print("Size: ",len(stack))