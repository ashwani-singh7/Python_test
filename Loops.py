
string = 'this is a string'

for x in string:
	print(x)

data = [1,3,5,6,7,9]

for y in data:
	print(y**2)

number = True

while number == True:
	print('you want a print')

	user_input = input('do you want to print again (y/n)')
	if user_input == 'n':
		number = False
	elif user_input=='y':
		number == True
	else:
		number = None 
		print('just answer yes or no Exiting now...')
