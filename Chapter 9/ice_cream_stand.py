class Restaurant:
	'''Create a class to describe a restaurant name and cuisine type'''
	def __init__(self, name, cuisine):
		self.name = name.title()
		self.cuisine = cuisine.title()


	def describe_restaurant(self):
		print(f"{self.name.title()} serves {self.cuisine.title()} food.")

	def open_restaurant(self):
		print(f"{self.name.title()} is now open!")

'''Child class of Restaurant'''
class IceCreamStand(Restaurant):
	def __init__(self, name, cuisine = 'ice_cream'):
		super().__init__(name, cuisine)
		self.flavors = []

	def display_flavors(self):
		print("\n We have the following flavors: ")
		for flavor in self.flavors:
			print("\t -" + flavor.title())

my_restaurant = IceCreamStand('ice cream dream', 'ice cream')
my_restaurant.flavors = ['chocolate', 'vanilla', 'strawberry']

my_restaurant.describe_restaurant()
my_restaurant.display_flavors()
