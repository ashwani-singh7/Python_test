
#employee = ['ashu','mohan','ankur','siddharth','shivam']

#name = input('enter the name or the reffal employee ')

def who_do_know():
	people = input('enter the list of people you know seprated by commas : ')
	people_list = people.split(',')
	print(people_list)
	return people_list



def ask():
	name = input('enter the name or the reffal employee ')
	
	if name in who_do_know():
		print('So you know {}!'.format(name))
	else:
		print('there is no employee such as {}!'.format(name))


ask()