#Create three dictionaries of people's info then store the dicitonaries in a list
people = []

person = {
	'first': 'isabella', 
	'last': 'fouquier', 
	'age': 15, 
	'city': 'white oak',
	}
people.append(person)

person = {
	'first': 'matthew', 
	'last': 'fouquier', 
	'age': 41, 
	'city': 'tampa',
	}
people.append(person)

person = {
	'first': 'amanda', 
	'last': 'braun', 
	'age': 39, 
	'city': 'tampa'
	}
people.append(person)

for person in people:
	name = person['first'].title() + " " + person['last'].title()
	age = str(person['age'])
	city = person['city'].title()

	print(name + " is " + age + " years old and lives in " + city + ".")