#def make_shirt(size='L', message="Provide a message"):
#	'''My attempt at 8-3 I used the input variable'''
#	size = input("What size shirt do you need: S,M,L,XL: ")
#	message = input("T-shirt message: ")
#	print(f"You have ordered a {size} shirt. With the message '{message}'")
#	return size, message

#make_shirt()
def make_shirt(size, message):
	"""The way the book says to make the function."""
	print(f"\nI'm going to make a {size} shirt.")
	print(f"The shirt should say {message} on the front.")

#make_shirt("L", "Python Rules!")
make_shirt(message="You can't touch this!", size="XL")

#Excercise 8-4 modifies 8-3 with default values for size and message.
def make_shirt(size="L", message="I love Python!"):
	print(f"\nI'm going to make a {size} shirt.")
	print(f"The shirt should say {message} on the front.")

make_shirt()
make_shirt("M")
make_shirt("S","Wokka Wokka")