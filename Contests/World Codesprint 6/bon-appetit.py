n,k = input().split()
cost = list(map(int,input().split(' ')))
charged = int(input())
actual_cost = 0
for index in range(int(n)):
    if(index==int(k)):
        continue
    actual_cost+=cost[index]

actual_cost/=2

if(actual_cost == charged):
    print ("Bon Appetit")
else:
    print (int(charged - actual_cost))
    
    
            
