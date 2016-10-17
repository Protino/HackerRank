#!/bin/python3

import sys


n,k = mao(int,input().split()]
arr = []
profits= []
losses = []
for i in range(n):
    x,y = map(int,input())
    profits.append(x)
    losses.append(y)
    arr.append((x-y),i)

sorted_arr = sorted(arr,key=lambda x: x[1])
profit = sum(sorted_arr[:k])
loss = 0
for i in range(k,n):
    loss_index= sorted_arr[i][1]
    loss+=losses[loss_index]

total = profit-loss
print (total) if total>0 else print (0)

    





    
    
    
