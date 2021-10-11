pizzas = ['supreme', 'hawaiian', 'meat lovers']

#Copy the original list
friends_pizza = pizzas[:]

#Add a pizza to the end of the original list
pizzas.append('veggie')
print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza.title())
print('\n')
#Add a pizza to friends pizza list
friends_pizza.append('sausage')
for friend in friends_pizza:
	print(friend.title())