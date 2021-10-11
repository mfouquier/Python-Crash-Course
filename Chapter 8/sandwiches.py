def sandwich_order(bread, meat, *toppings):
	print(f"We will make a {meat} sandwich on {bread} bread with the following toppings: ")
	for topping in toppings:
		print(f"- {topping}")
sandwich_order('white', 'turkey', 'lettuce','pickle','mayo')