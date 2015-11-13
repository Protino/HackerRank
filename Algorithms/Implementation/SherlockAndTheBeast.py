for _ in range(int(raw_input())):
    y=int(raw_input()) 
    z=y 
    while(z%3!=0):
        z-=5 
    if(z<0): 
        print '-1' 
    else: 
        print z*'5'+(y-z)*'3'
		