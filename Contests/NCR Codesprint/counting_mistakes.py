
n = int(input().strip())
oriArr=[int(x) for x in input().split()]
expArr=[x for x in range(oriArr[0],n+oriArr[0])]
print (sum(i!=j for i,j in zip(oriArr,expArr))+1*(oriArr[0]!=1))
