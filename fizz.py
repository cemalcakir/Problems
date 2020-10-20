def fizzBuzz(**kwargs):
	for i in range(1, 101):
		output = ""
		for key, value in kwargs.items():
			if not i % value:
				output += key
		print(output or i)

fizzBuzz(Fizz = 3, Buzz = 5)
