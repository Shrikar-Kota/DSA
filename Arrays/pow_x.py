'''
Problem statement:

Find x^n given x can be any value and n is an integer.
'''

def pow(x, y):
    if y == 0:
        return 1
    if y < 0:
        return 1/pow(x, -y)
    return x*pow(x*x, y//2) if y%2 else pow(x*x, y//2)

print(pow(3, 5))