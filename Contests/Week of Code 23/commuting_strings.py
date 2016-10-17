def computeLPSArray(string, M, lps):
    length = 0
    i = 1
    lps[0] = 0
    while i < M:
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
 
def symmetricString(string,n):
    lps = [0] * n
    computeLPSArray(string, n, lps)

    length = lps[n-1]
    
    if length > 0 and n%(n-length) == 0:
        return (n-length)
    else:
        return (n)

s = input()
m = int(input())
len_s = len(s)
mod = 10**9 + 7
pos_t = 0
count = 0

if(len_s>m):
    print (0)
elif(s == len_s * s[0]):
    print ((m - len_s + 1)%mod)
else:
    start_len = symmetricString(s,len_s)
    while(pos_t<=m):
        pos_t=pos_t+start_len
        count+=1
    print (count-1)
    
    
