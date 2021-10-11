class Restaurant:
	'''Create a class to describe a restaurant name and cuisine type'''
	def __init__(self, name, cuisine):
		self.name = name.title()
		self.cuisine = cuisine.title()


	def describe_restaurant(self):
		print(f"{self.name.title()} serves {self.cuisine.title()} food.")

	def open_restaurant(self):
		print(f"{self.name.title()} is now open!")

'''Instance #1'''
restaurant = Restaurant("olive garden", "italian")

print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()


'''Instance #2'''
thai = Restaurant('bangkok', 'thai')

print("\n")
print(thai.name)
print(thai.cuisine)

thai.describe_restaurant()
thai.open_restaurant()

'''Instance #3'''
american = Restaurant('hooters', 'american')

print("\n")
print(american.name)
print(american.cuisine)

american.describe_restaurant()
american.open_restaurant()