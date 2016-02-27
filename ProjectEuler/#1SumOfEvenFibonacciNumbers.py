import math
phi = 1.6180339887498948482045868343656
phiCube = phi**3
rootFive = 1/(5**0.5)
InversephiCube = 1/phi
def computeSum(k):
    firstTerm = phiCube*((1-(phiCube)**k)/(1-phiCube))
    secondTerm = InversephiCube*((1-(-InversephiCube)**k)/(1+InversephiCube))
    evenSum = rootFive*(firstTerm + secondTerm)
    print (round(evenSum))

def fibonacciIndex(F):
    print (math.log(F*math.sqrt(5))/math.log(phi)+ 0.5)

computeSum(2)

fibonacciIndex(6)
    
