from fibonacci import fibonacci
n = -1
def nextFib():
    global n
    n += 1
    return fibonacci(n)

def createFibSeq():
    a = 0
    b = 1

    def otherNextFib():
        nonlocal a, b
        ret = a
        a, b = b, a + b
        return ret
    
    return otherNextFib

awesomeSauce = createFibSeq()
for _ in range(10):
    print(str(awesomeSauce()))
