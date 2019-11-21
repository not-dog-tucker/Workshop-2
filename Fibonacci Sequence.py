def fibonacci(i):
    j = 0
    a = 0
    b = 1
    while j < i:
        c = a + b
        a = b
        b = c
        j+=1
    print(str(c))
    

