mod = 10**9+7

'''
Given the input string, parse it
and return formatted expression
input - 2**33242*3242
output - [2,**,33232,*,3242]
'''
def parse(e):
    #Check if end characters are digits
    if (e[len(e)-1]=="*" or e[0]=="*"):
        return False

    expr = []
    asteriskCount = 0
    
    for ch in e:
        if ch.isdigit():
            #If prev character is a digit concat
            #else start a new number
            if expr and expr[-1].isdigit():
                expr[-1]+=ch
            else:
                expr.append(ch)
            asteriskCount = 0
        else:
            #If prev char is * then concat to make **
            if expr and expr[-1]=="*":
                expr[-1]+=ch
            else:
                expr.append(ch)
            asteriskCount+=1
            #multiple * check
            if asteriskCount>2:
                return False
    return expr

'''
Simplify the expression by calculating
exponents.
i.e, [2,**,33232,*,3242] - > [43244609,*,3242]
'''
def simplify(expr):
    i=0
    while i<len(expr):
        token = expr[i]
        if token=="**":
            simpleExpr.append(pow(int(simpleExpr.pop()),int(expr[i+1]),mod))
            i+=2
        else:
            simpleExpr.append(token)
            i+=1

    return expr

for __ in range(int(input())):

    expr = parse(input())

    if not expr:
        print ("Syntax Error")
        continue

    expr = simplify(expr)
    
    #Now, just multiply the remaining numbers
    result = 1
    for token in simpleExpr:
        if token!="*":
            result=(result*int(token))%mod
    print (result%mod)
        
                
                
            
        
                    
            
        
                
