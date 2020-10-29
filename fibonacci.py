# A very basic script to print out Fibonacci numbers.
a = 0
b = 1
x = 20

for i in range(x):
    print(a)
    a, b = b, a+b
