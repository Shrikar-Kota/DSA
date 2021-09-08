'''
Check for balanced paranthesis.
'''
string = "()[]{}{(()[[])}"
stack = []
opening = ['(', '{', '[']
closing = [')', '}', ']']
flag = "balanced"
for i in string:
    if i in opening:
        stack.append(i)
    else:
        if opening.index(stack.pop()) != closing.index(i):
            flag = "Not balanced"
            break
print(flag)
