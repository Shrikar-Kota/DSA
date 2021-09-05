'''
Problem Statement:

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

'''
s = [7,1,5,3,6,4]
#peak valley approach
'''
7 is a peak so we dont buy.

1 is a valley, so we buy there.
5 is a peak, we sell there.

3 is a valley, buy.
6 is a peak, sell.
'''
cp = -1
profit = 0
for i in range(len(s)):
    if (i == 0 or s[i] >= s[i-1]) and (i == len(s)-1 or s[i] > s[i+1]) :
        if cp != -1:
            profit += s[i] - cp
            cp = -1
    elif (i == 0 or s[i] <= s[i-1]) and (i == len(s)-1 or s[i] <= s[i+1]):
        if cp == -1:
            cp = s[i]
print(profit)

#simpler
'''
instead of tracking peaks and valleys, we sell whenever the stock price in next day is high
'''
profit = 0
for i in range(1, len(s)):
    if s[i] > s[i-1]:
        profit += s[i] - s[i-1]
        
print(profit)