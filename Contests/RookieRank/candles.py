from random import randint
dummy = int(input())
#candles = list(map(int,input().split()))
candles = [randint(0,10) for __ in range(10**3)]

print (sorted(candles))

largest_count = 0
largest=candles[0]

for candle in candles:
    if largest <= candle:
        largest = candle
        largest_count+=1

print (largest_count)
