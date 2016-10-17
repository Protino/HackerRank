#!/bin/python3

import sys


n,k = map(int,input().split())
arr = []
profits= []
losses = []
for i in range(n):
    x,y = map(int,input().split())
    profits.append(x)
    losses.append(y)
    arr.append(((x-y),i))

sorted_arr = sorted(arr,key=lambda x: x[0],reverse=True)
profit = 0
loss = 0
for i in range(n):
    if (i>k-1):
        index= sorted_arr[i][1]
        loss+=losses[index]
    else:
        index= sorted_arr[i][1]
        profit+=profits[index]
        
        

total = profit-loss
print (total) if total>0 else print (0)

    





    
    
    
