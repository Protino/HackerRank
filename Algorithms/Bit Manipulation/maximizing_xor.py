#!/usr/bin/python3
def maxXor(l, r):
    bin_l = bin(l)[2::]
    bin_r = bin(r)[2::]
    if len(bin_l) == len(bin_r):
        while bin_l[0]==bin_r[0]:
            bin_l = bin_l[1:]
            bin_r = bin_r[1:]
        return 2**(len(bin_r))-1
    return 2**len(bin_r)-1
        
        
        
if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))
