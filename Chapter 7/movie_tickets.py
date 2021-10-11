age = "\nHow old are you? "
age += "\nEnter 'done' when you are finished. "

while True:
	price = input(age)
	
	if price == 'done':
		break
	price = int(price)
	
	if price < 3:
		print("Your ticket is free.")

	elif price < 13:
		print("Your ticket is $10.")

	else:
		print("Your ticket is $15.")