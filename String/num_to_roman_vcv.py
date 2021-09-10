'''
Problem statement:

- convert roman to decimal.
- convert decimal to roman.

'''

#1
r = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V':5,'I': 1, '0': 0}
sum = 0
prev = '0'
for i in s:
    if i != 'I':
        if r[prev] < r[i]:
            sum -= 2*r[prev]
    sum += r[i]    
    prev = i
print(sum)

#2
i = 0
out = ""
l = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
for i in d:
    if num//i > 0:
        out = out + d[i]*(num//i)
    num = num%i
print(out)