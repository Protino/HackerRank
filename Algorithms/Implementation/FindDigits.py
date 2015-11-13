for __ in range(int(input())):
    num = input()
    count=0
    for digit in num:
        digit = int(digit)
        if((digit!=0)and(int(num) % digit==0)):
            count=count+1
    print (count)
        