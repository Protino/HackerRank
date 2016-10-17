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
 
def symmtericString(string):
    n = len(string)
    lps = [0] * n
    computeLPSArray(string, n, lps)

    length = lps[n-1]
 
    # If there exist a suffix which is also prefix AND
    # Length of the remaining substring divides total
    # length, then str[0..n-len-1] is the substring that
    # repeats n/(n-len) times (Readers can print substring
    # and value of n/(n-len) for more clarity.
    if len > 0 and n%(n-length) == 0:
        return True
    else:
        False
 
# Driver program
txt = ["ABCABC", "ABABAB", "ABCDABCD", "GEEKSFORGEEKS",
        "GEEKGEEK", "AAAACAAAAC", "ABCDABC"]
n = len(txt)
for i in xrange(n):
    if isRepeat(txt[i]):
        print ("True")
    else:
        print ("False")
 
# This code is contributed by BHAVYA JAIN
