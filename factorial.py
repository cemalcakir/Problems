x = int(input("Factorial of: "))

def factorial(number):
	if number < 0:
		return "Enter a positive integer."
	else:
		# Base case
		if number == 0:
			return 1
		# Recursive case
		else:
			return number * factorial(number - 1)

print(factorial(x))
