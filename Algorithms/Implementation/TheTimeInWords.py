#!/bin/python

import sys
#initialize words
words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","quarter","sixteen","seventeen","eighteen","nineteen","twenty",
            "twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","thirty","thirty one","thirty two","thirty three","thirty four","thirty five",
            "thirty six","thirty seven","thirty eight","thirty nine","forty","forty one","forty two","forty three","forty five","forty six","forty seven","forty eight","forty nine","fifty","fifty one","fifty two",
            "fifty three","fifty four","fifty five","fifty six","fifty seven","fifty eight","fifty nine","sixty"]

#input values
h = int(input().strip())
m = int(input().strip())

#convert to words
H = words[h]
M = words[m]


if(m == 0):
    print (H + " o' clock")
elif(m == 15):
    print ("quarter past " + H)
elif(m == 30):
    print ("half past " + H)
elif(m == 45):
    if (h  < 12):
        print ("quarter to " + words[h+1])
    else:
        print ("quarter to one")

elif(m<30):
    if(m < 10):
        print (M + " minute past " + H)
    else:
        print (M + " minutes past " + H)

else:
    M = words[60-m]
    print (M + " minutes to " + words[h+1])
