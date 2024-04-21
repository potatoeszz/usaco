#write a function to calculate a factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
#this is an example of recursive (using the function to define itself)

def factorial_WithLoop(n):
    res = 1
    while n > 1:
        res = n * res
        n = n - 1
    return res
#this is an example of iterative (using a loop)

#def factorial(n):
    #if n>1:
        #n *= n-1
        #return n
    #elif n == 1:
         #return n
#^ this is my failed code XD

        
print(str(factorial_WithLoop(5)))
#f5 = factorial(5)