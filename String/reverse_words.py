'''
Problem statement:

- Reverse words in a string.
- Reverse the position of the words
'''

#Reverse words
string = "Hello World"
string = list(string)
string.append(" ")
prev = -1
for i in range(len(string)):
    if string[i] == " ":
        if prev != -1:
            string[prev:i] = string[prev:i][::-1]
        prev = -1
    else:
        if prev ==- 1:
            prev = i
string = "".join(string[:-1])
print(string)

#Reverse position
string = "Hello World"
string = list(string)
string = string[::-1]
string.append(" ")
prev = -1
for i in range(len(string)):
    if string[i] == " ":
        if prev != -1:
            string[prev:i] = string[prev:i][::-1]
        prev = -1
    else:
        if prev == -1:
            prev = i
    
string = "".join(string[:-1])
print(string)