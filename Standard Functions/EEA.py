'''
Returns gcd(b,n),x,y where gcd(b,n)=xb+yn
'''
def eea(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

print (eea(258,147))

    
    
    
