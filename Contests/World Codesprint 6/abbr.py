# Enter your code here. Read input from STDIN. Print output to STDOUT
class PrintNo(Exception ):
    pass
for __ in range(int(input())):
    a = list(input())
    temp_b = list(input())
    i=0
    j=0
    temp = []
    b = [x for x in temp_b]
    limit_b = len(b)
    try:
        for char in a:
            if char.upper() in temp_b:
                temp.append(char)
                if char.isupper():
                    temp_b.remove(char)
            else:
                if (char.isupper()):
                    raise PrintNo
        limit_a = len(temp)
        while (j<limit_b):
            while (i<limit_a):
                if temp[i].isupper() and temp[i]!=b[j]:
                    raise PrintNo
                if temp[i].upper() == b[j]:
                    count = 0
                    while (b[j]==temp[i].upper()):
                        count+=1
                        i+=1
                        if (i==limit_a):
                            i-=1
                            break
                    count-=1
                    if (j==limit_b-1):
                        j+=1
                        break
                    while (b[j]==b[j+1] and count>0):
                        count-=1
                        j+=1
                        if (j>=limit_b-1):
                            break
                    j+=1
                    break
                i+=1
            if i==limit_a and j<limit_b:
                print ("crossed",i,j)
                raise PrintNo
        print ("YES")
    except PrintNo:
        print ("NO")
        pass


