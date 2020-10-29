# A very basic script to print Fibonacci numbers.
a = 0
b = 1
# Value cap
while a < 1000:
    print(a)
    a, b = b, a+b
