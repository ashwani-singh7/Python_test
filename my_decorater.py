import functools

def my_decorator(func)
	@functools.wrap(func)
	def function_that_runs_func()
		print('in the decodator')
		func()
		print(after the decodator)
	return function_that_runs_func

@my_decorator
def my_function():
	print("this is the main function")

my_function