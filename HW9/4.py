import time
import logging
logging.basicConfig(filename='log_msg.logs', level=logging.DEBUG)


"""
Returns a memoized version of f
def memoize(f):
    memory = {}
    def memoized(*args):
        if args not in memory:
            memory[args] = f(*args)
        return memory[args]
    return memoized
"""

def clock(func):
    def clocked(*args):
        """ Clocking decoration wrapper """
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        logging.info(f"{elapsed} = {name}:{args} ==> {result}")
        return result
    return clocked


cache_fact = {0: 1, 1: 1}


@clock
def factorial(input_value, cache=cache_fact):
    assert input_value >= 0
    if input_value in cache:
        print("cached before")
        return cache[input_value]
    print("caching")
    cache[input_value] = input_value * factorial(input_value - 1)
    return cache[input_value]


cache_fib = {0: 0, 1: 1}


@clock
def fibonacci_of(n, cache=cache_fib):
    assert n >= 0
    if n in cache:  # Base case
        print("cached before")
        return cache[n]
    # Compute and cache the Fibonacci number
    print("caching")
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]


print(fibonacci_of(10))
print(fibonacci_of(5))
print(fibonacci_of(6))
print(fibonacci_of(5))
print(fibonacci_of(10))

print(factorial(5))
print(factorial(2))
print(factorial(3))
print(factorial(7))
print(factorial(10))

