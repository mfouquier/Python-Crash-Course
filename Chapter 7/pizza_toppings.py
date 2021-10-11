prompt = "\nWhat toppings would you like on your pizza? "
prompt += "\nWhen you are finished type 'done' "


while True:
	topping = input(prompt)

	if topping == 'done':
		break
	else:
		print(f"\nWe will add {topping}. What else would you like?")