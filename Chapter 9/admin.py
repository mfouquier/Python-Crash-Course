class User:
	def __init__(self, first_name, last_name, hometown, age, status):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.hometown = hometown.title()
		self.age = age
		self.status = status
		self.login_attempts = 0

	def increment_login_attempts(self):
		self.login_attempts += 1
		print(f"You have attempted to login {self.login_attempts} times.")

	def describe_user(self):
		print(f"My name is {self.first_name} {self.last_name} and I am from {self.hometown}. I am {str(self.age)} years old and I am {self.status}.")

	def reset_login_attempts(self):
		self.login_attempts = 0
		print(f"Your login attempts have been reset.")

class Admin(User):

	def __init__(self, first_name, last_name = 'none', hometown = 'none', age = 'none', status = 'none'):
		super().__init__(first_name, last_name, hometown, age, status)
		self.privileges = Privileges()

	'''def show_privileges(self):
		print("\nAs an Admin you are able to do the following: ")
		for priv in self.privileges:
			print("\t -" + priv)'''

#admin = Admin('Administrator')
#admin.privileges = ['Delete posts', 'Boot users', 'Kick all the ass']
#admin.describe_user()
#admin.show_privileges()

class Privileges:
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		print("\nPrivileges:")
		if self.privileges:
			for privilege in self.privileges:
				print("- " + privilege)
			else:
				print("- This user has no privileges.")

admin = Admin('Administrator')
admin.describe_user()

admin.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
admin.privileges.privileges = eric_privileges
admin.privileges.show_privileges()