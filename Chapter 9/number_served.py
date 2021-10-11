#Modifies restaurant from 9.1 and adds the number served attribute
class Restaurant:
	'''Create a class to describe a restaurant name and cuisine type'''
	def __init__(self, name, cuisine):
		self.name = name.title()
		self.cuisine = cuisine.title()
		self.number_served = 0


	def describe_restaurant(self):
		print(f"{self.name.title()} serves {self.cuisine.title()} food.")

	def open_restaurant(self):
		print(f"{self.name.title()} is now open!")

	def number_people_served(self, number_served):
		self.number_served = number_served
		print(f"We have served {self.number_served} customers.")

	'''def set_the_number(self):
		set_number = input("How many customers were served today? ")
		return print(f"As of today we have served {set_number} of customers.")'''
	def increment_number(self, customers):
		self.number_served += customers 
		print(f"We have now served {self.number_served}!")
	

'''Instance #1 of number served'''
customers_served = Restaurant('chilis', 'american')
customers_served.describe_restaurant()

customers_served.number_people_served(545)

customers_served.increment_number(15)
