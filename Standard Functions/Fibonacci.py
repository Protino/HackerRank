fibTable = {1:1, 2:1}
evenSum = 0 
def fib(n):
   if n <= 2:
      return 1
   if n in fibTable:
      return fibTable[n]
   else:
      fibTable[n] = fib(n-1) + fib(n-2)
      return fibTable[n]


def fibSum(limit):
   last = 1
   secondLast = 1
   evenSum = 0
   for __ in range(limit-1):
      temp = last
      last = last + secondLast
      secondLast = temp

      if(last%2==0):
         evenSum+=last
   return evenSum

def fibonacci_iter(limit):
    a, b = 0, 1
    for __ in range(limit):
        yield a
        a, b = b, a + b

print (sum(a for a in fibonacci_iter(10000) if not (a & 1)))

fib(10)

print (fibTable.values())

print (fibSum(100))



