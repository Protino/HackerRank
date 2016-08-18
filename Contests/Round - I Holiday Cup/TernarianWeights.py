import math
def calculateExponent(wt):
    if(wt==0):
        return 1
    if(wt==1 or wt<0):
        return 0
    return int(round(math.log(wt,10)/log3))


for __ in range(int(input())):
    log3 = 0.47712125471966244
    objWt = int(input())
    leftPanWt = objWt
    rightPanWt = 0
    leftPan = []
    rightPan = []
    expo = calculateExponent(objWt)
    print (expo)
    while (leftPanWt!=rightPanWt):
        add = 3 ** expo
        if(rightPanWt<leftPanWt):
            try:
                length=len(rightPan)-1
                lastElement = rightPan[length]
                if(lastElement==add):
                    rightPan[length]=rightPan[length]+add
                    rightPanWt+=add 
                else:
                    rightPan.append(add)
                    rightPanWt+=add    
            except:
                rightPan.append(add)
                rightPanWt+=add
            
        else:
            leftPan.append(add)
            leftPanWt+=add

        if(rightPanWt<leftPanWt):
            expo=calculateExponent(leftPanWt-rightPanWt)
        else:
            expo=calculateExponent(rightPanWt-leftPanWt)
    print ("left pan:"," ".join(map(str,leftPan)))
    print ("right pan:"," ".join(map(str,rightPan)))
    print ("")
	
