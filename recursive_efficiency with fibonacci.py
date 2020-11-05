# A very basic script to print out Fibonacci numbers.

x = 10

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_timer
def fibonacci_for(number):	
	a = 0
	b = 1
	for i in range(20):
    	# print(a)
		a, b = b, a+b
	return a
print(fibonacci_for(x))

@my_timer
def fibonacci_recursive(number):
	if number == 0:
		return 0
	if number == 1:
		return 1
	else:
		return fibonacci_recursive(number - 2) + fibonacci_recursive (number - 1)

# print(fibonacci_recursive(x))
