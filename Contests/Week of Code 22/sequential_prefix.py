string = []
prefix_array = []
j=0
i=-1
n = int(input().strip())
for k in range(n):
    query  = [x for x in input().strip().split(' ')]
    if query[0]=='+':
        string.append(query[1])
        i+=1
    else:
        
        string=string[:-1]
        prefix_array=prefix_array[:-1]
        print (j+1)
        if i <= 0:
            j=0
        else:
            i-=1
            j=prefix_array[i]-1
        continue

    #completed    
    if len(string)<2:
        prefix_array.append(0)
        print (0)
        continue

    #completed
    while True:
        if string[j] == string[i]:
            prefix_array.append(j+1)
            print (j+1)
            j+=1
            break
        else:
            if j==0:
                prefix_array.append(0)
                print (0)
                i+=1
                break
            else:
                j=prefix_array[j-1]
