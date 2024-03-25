#Basic Function

def delta(a,b,c):
  deltaValue = b*b-4*a*c
  return deltaValue

print(delta(4,3,2))

#Function with arbitrary parameters

def myprint(*words):
    for word in words:
        print(word)
    

myprint("testing", "my", "print", "function")

#Function argument keyword

def liftCalculus(ro, speed, area, liftCoeficient):
  lift = 0.5*ro*speed*speed*area*liftCoeficient
  print("Your lift is",lift)

liftCalculus(ro = 1, speed = 10, area = 2, liftCoeficient=1)

#Function arbitrary keyworkds
def myRectangle(**format):
  print("The rectangle color is " + format["color"])

myRectangle(height = 12, widht = 10, color = "Black")

#Function widh default parameters

def myFunction(country = "Brazil"):
    print("I am from "+ country)

myFunction()

#Function with positional only arguments

def powFunction(x,/):
    print(x*x)

powFunction(3)

#Function with keywork only arguments

def keywordFunction(*,x):
    print(x)

keywordFunction( x = 2)

#Function combined keyword and positional

def combinedFunction(a, b, /, *, c, d):
  print(a + b + c + d)

combinedFunction(5, 6, c = 7, d = 8)

#Function recursion

def fibonacci(k):
    if(k == 1):
        return 1
    elif(k == 2):
        return 1
    elif(k > 2):
        return fibonacci(k-1)+fibonacci(k-2)
    else:
        return 0;

fibonacciPosition = 8
print("Fibonacci of: "+str(fibonacciPosition)+" is "+ str(fibonacci(fibonacciPosition)))
        