prompt = "How old are you? "
prompt += "\nEnter 'quit' when you are finished. " 

age = str("")

while age != 'quit':
	age = input(prompt)
	age = int(age)

	if age == 'quit':
		age = str(age)

	if age < 3:
		print("Free Ticket")
	elif age < 13:
		print("$10 Ticket")
	else:
		print("$15 Ticket")