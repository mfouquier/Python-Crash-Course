#Create a FOR loop that lists out the different types of pizza in the list.
pizzas = ['supreme', 'hawaiian', 'meat lovers', 'pepperoni', 'sausage', 'cheese']
#for pizza in pizzas:
#	print(f"Give me a {pizza.title()} pizza and I will be happy.")
#print("Pizza is the best!")

#Use SLICES on a previous project from Chapter 4. Project above.

#Print the first three items using SLICE
print("The first three items in the list are:")
for pizza in pizzas[:3]:
	print(pizza.title())
print("\n")

#Print items from the middle of the list using SLICE
print("These are items from the middle of the list:")
for pizza in pizzas[1:4]:
	print(pizza.title())
print("\n")

#Print the last three items using SLICE
print("These are the last items in the list:")
for pizza in pizzas[-3:]:
	print(pizza.title())