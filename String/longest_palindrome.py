'''
Problem statement:

- Longest Palindrome
'''

#reverse the string and find the common substring
s = 'abcbcadefa'
maxlen = s[0]
reverse = s[::-1]
for i in range(len(s)):
    for j in range(len(reverse)):
        end = j
        start = i
        length = 0
        while (start < len(reverse) and end < len(reverse)):
            if s[start] != reverse[end]:
                break
            end += 1
            start += 1
            length += 1
        if length and i == len(reverse) - end:
            if len(maxlen) < length:
                maxlen = s[i:start]
print(maxlen)

