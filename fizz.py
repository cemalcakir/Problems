"""A program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz."""

def fizzBuzz(**kwargs):
	for i in range(1, 101):
		output = ""
		# Can not use integers as key in **kwargs
		for key, value in kwargs.items():
			if not i % value:
				output += key
		print(output or i)

fizzBuzz(Fizz = 3, Buzz = 5)
