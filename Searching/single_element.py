'''
Problem statement:

Every element repeats twice, except for one element. Array is sorted.
'''

l = [1, 1, 2, 3, 3, 4, 4]

#Naive
for i in range(0, len(l)-1, 2):
    if l[i]!=l[i+1]:
        break
print(l[i])

#Optimal

low = 0; high = len(l) - 1
while low <= high:
    mid = (low+high)//2
    if (mid != 0 and l[mid] == l[mid-1]):
        if mid%2:
            low = mid + 1
        else:
            high = mid - 1
    elif mid != len(l)-1 and l[mid] == l[mid+1]:
        if mid%2:
            high = mid - 1
        else:
            low = mid + 1
    else:
        print(l[mid])
        break