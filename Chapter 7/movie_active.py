prompt = "How old are you? "
prompt += "\nEnter 'quit' when you are finished. " 

flag = True

while flag: 
	age = input(prompt)

	if age == "quit":
		flag = false
	age = int(age)

	if age < 3:
		print("Free Ticket!")
	elif age < 13:
		print('$10 Ticket.')
	else:
		print('$15 Ticket.')