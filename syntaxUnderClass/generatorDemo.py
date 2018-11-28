
generator_ex = (x*x for x in range(10))

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n +=1