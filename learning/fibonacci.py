#find how to locate what number is at the nth spot of the fibonacci sequence
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
