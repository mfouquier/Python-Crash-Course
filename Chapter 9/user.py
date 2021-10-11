class User:
	def __init__(self, first_name, last_name, hometown, age, status):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.hometown = hometown.title()
		self.age = age
		self.status = status


	def describe_user(self):
		print(f"My name is {self.first_name} {self.last_name} and I am from {self.hometown}. I am {str(self.age)} years old and I am {self.status}.")


	def greet_user(self):
		print(f"{self.first_name} {self.last_name} welcome to the forum!")

'''Instance #1'''
matt = User('matt', 'fouquier', 'morgan city', 41, 'married')		

matt.describe_user()
matt.greet_user()

'''Instance #2'''
amanda = User('amanda', 'braun', 'green bay', 39, 'married')
print("\n")
amanda.describe_user()
amanda.greet_user()

'''Instance #3'''
bill = User('bill', 'mccoy', 'houston', 44, 'single')
print("\n")
bill.describe_user()
bill.greet_user()