stack = []
formula = input().split()
for c in formula:
    if c == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b) + int(a))
    elif c == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b) - int(a))
    elif c == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(int(b) * int(a))
    else:
        stack.append(int(c))

print(stack.pop())



