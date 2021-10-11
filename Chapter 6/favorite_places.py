#Nest lists in a dictionary - Treat each item in the list as an individual item, i.e. put it in QUOTES!

places = {
	'matt': ['germany', 'china', 'australia'], 
	'amanda': ['ireland', 'france'], 
	'chase': ['green bay', 'yellowstone'],
	}

#Create variables for the key-value pairs and print out each person's favorite places.
for name, values in places.items():
	print('\nThese are ' + name.title() + "'s favorite places:")
	for value in values:
		print('-' + value.title())