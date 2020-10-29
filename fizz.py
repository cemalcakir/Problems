"""Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”."""

def fizzBuzz(**kwargs):
	for i in range(1, 101):
		output = ""
		# Keys can not be integers in Python dictionaries, so I used value as key.
		for key, value in kwargs.items():
			if not i % value:
				output += key
		print(output or i)

fizzBuzz(Fizz = 3, Buzz = 5)
