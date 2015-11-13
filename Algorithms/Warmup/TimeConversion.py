time=str(input())
newtime=time[2:8]
append=int(time[0:2])
period=time[8]
if (period!='A'):
    if(append<12):
        append=12+append
    print (str(append)+newtime)
else:
    if(append==12):
        print ("00"+newtime)
    else:
        print (time[0:8])
