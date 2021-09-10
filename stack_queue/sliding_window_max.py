'''
Problem statement:

Find maximum of all the windows of size k.
'''
#Naive
nums = [1,3,-1,-3,5,3,6,7]; k = 3
a = [0 for i in range(len(nums)-k+1)]
for i in range(len(nums)-k+1):
    a[i] = max(nums[i:i+k])
print(a)

#Better
queue = deque([])
a = [0 for i in range(len(nums)-k+1)]
for i in range(k):
    while queue and nums[queue[-1]] <= nums[i]:
        queue.pop()   
    queue.append(i) 
a[0] = nums[queue[0]]
for i in range(k, len(nums)):
    if queue[0] <= i - k:
        queue.popleft()
    while queue and nums[queue[-1]] <= nums[i]:
        queue.pop()
    queue.append(i)    
    a[i-k+1] = nums[queue[0]]

print(a)
