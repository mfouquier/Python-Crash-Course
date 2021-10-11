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

new_user = User('matt', 'foo', 'here', 4, 'killing it')
new_user.describe_user()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()

new_user.reset_login_attempts()
print(new_user.login_attempts)

