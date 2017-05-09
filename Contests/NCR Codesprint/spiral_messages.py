import re
def rotate_matrix(arr):
    return [list(reversed(list(x))) for x in zip(*arr)]
    
def spiral_traverse(arr):
    words=''
    while arr:
        words+=''.join(arr[0])
        arr=list(reversed(list(map(list,zip(*arr[1:])))))
    words = re.sub(r'\W+', '#', words)
    print (len([x for x in words.split('#') if x!='']))

m,n=map(int,input().split())
arr=[]
for i in range(m):
    arr.append(list(input()))
spiral_traverse(rotate_matrix(arr))
