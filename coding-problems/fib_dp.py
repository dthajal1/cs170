# Naive fib
def fib(n):
    if n <= 1: 
        return n
    else:
        return fib(n-1) + fib(n-2)

# even fib(40) takes a while
# print(fib(40))

# Top Down (Recursion + Memoization)
# - Recursion + lookup table to not have to recompute f(.) multiple times on same arguments
def fibMemo(n, mem):
    if n <= 1:
        return n
    elif mem[n] != None:
        return mem[n]
    else:
        mem[n] = fibMemo(n-1, mem) + fibMemo(n-2, mem)
        return mem[n]

def fibTopDown(n):
    mem = [None] * (n+1)
    return fibMemo(n, mem)

# even fibTopDown(100) is instant
# print(fibTopDown(100))


# Bottom Up (Mem table + iteration)
# - fill up the lookup table iteratively instead of recursively
# - runtime is the same but sometime this method can be memory efficient
def fibBottomUp(n):
    mem = [None] * (n+1)
    mem[0] = 0
    mem[1] = 1
    for i in range(2, n+1):
        mem[i] = mem[i - 1] + mem[i -2]
    return mem[n]

# even fibBottomUp(100) is instant
# print(fibBottomUp(100))


# Bottom Up Space Saving 
# - runtime is the same but sometime this method can be memory efficient
def fibBottomUpSpaceSaving(n):
    mem = [0, 1] # stores mem[i - 1] and mem[i - 2]
    for i in range(2, n+1):
        x = mem[0] + mem[1]
        mem[0] = mem[1]
        mem[1] = x
    return mem[1]

# even fibBottomUpSpaceSaving(100) is instant
print(fibBottomUpSpaceSaving(100))