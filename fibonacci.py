def fibonacci_for(number):
    # A very basic script to print out Fibonacci numbers.
    a = 0
    b = 1
    for _ in range(number):
        # print(a)
        a, b = b, a+b
    return a


def fibonacci_recursive(number):
    # Recursive function to call the nth fibonacci number, it takes a lot of time to calculate if n > 30
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonacci_recursive(number - 2) + fibonacci_recursive(number - 1)


"Yeni branch deneme"
