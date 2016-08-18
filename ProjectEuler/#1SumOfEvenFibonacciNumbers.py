import math
phi = (1 + math.sqrt(5))/2
phiCube = phi**3
rootFive = 1/(5**0.5)
InversephiCube = 1/phi
def computeSum(k):
    firstTerm = phiCube*((1-(phiCube)**k)/(1-phiCube))
    secondTerm = InversephiCube*((1-(-InversephiCube)**k)/(1+InversephiCube))
    evenSum = rootFive*(firstTerm + secondTerm)
    print (round(evenSum))

def fibonacciIndex(F):
    return (round(math.log(((F*math.sqrt(5)+math.sqrt(5*(F**2)-4))/2),phi)))

fib_series = [0,1]
fib1=1
fib2=2
for __ in range(1000):
    fib = 4*fib1+fib2
    fib1 = fib2
    fib2 = fib
    fib_series.append(fib)
    


def checkClosedForm(n):
    root5 = math.sqrt(5)
    a = ((root5*((2-root5)**n))-3*((2-root5)**n)+root5*((root5+2)**n)+3*((root5+2)**n)-2*root5)
    b = 2*root5*(root5-1)*(root5+1)
    return -a/b

def solveByUsingRecurrence(limit):
    """
    E(n) = 4*E(n-1) + E(n-2)
    """
    a0 = 0
    a1 = 2
    sumOfEvenFib = 2
    while(True):
        evenFib = 4*a1+a0
        if evenFib > limit -1:
            break
        a0 = a1
        a1 = evenFib
        sumOfEvenFib+=evenFib

    return sumOfEvenFib
        
        
print (solveByUsingRecurrence(10))
