n = int(input())
arr = [int(x) for x in input().split()]
muls = []
mod=10**9+7
base=pow(2,n,mod)-1
initial=n-2
correction=1
count=((base*arr[0])+(base*arr[n-1]))
two_pow=1
if (n==1):
    print (arr[0])
elif (n%2!=0):
    for i in range(1,(n//2)+1):
        print (i)
        base+=pow(2,initial,mod)-correction
        muls.append(base)
        count+=base*arr[i]
        initial-=1
        correction=pow(2,two_pow ,mod)
        two_pow+=1
    
    j=len(muls)-2
    print (muls)
    for i in range((n//2)+1,n-1):
        print (i)
        count+=muls[j]*arr[i]
        j-=1
    print (count%mod)
else:
    for i in range(1,(n//2)):
        print (i)
        base+=pow(2,initial,mod)-correction
        muls.append(base)
        count+=base*arr[i]
        initial-=1
        correction=pow(2,two_pow ,mod)
        two_pow+=1
    
    j=len(muls)-1
    for i in range((n//2),n-1):
        print (i)
        count+=muls[j]*arr[i]
        j-=1

    print (count%mod)
