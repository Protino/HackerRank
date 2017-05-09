
def countSubs(s):
    n = len(s)
    masks = [1<<j for j in range(n)]
    count=0
    for i in range(1,2**n):
        ss =  [s[j] for j in range(n) if (masks[j] & i)]
        if ss.count('a') == ss.count('b') and ss.count('c') == ss.count('d'):
            count+=1

    return count%(9+10**7)
        

# Return the number of non-empty perfect subsequences mod 1000000007
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = countSubs(sorted(s))
    print(result)
