#Store five names and their favorite numbers in a dictionary
favorite_numbers = {'eric':55, 'tony':93, 'sarah':23, 'melissa':85, 'matt':32,}

#Inserts the key and value using the format function
print(f"Eric's favorite number is {favorite_numbers['eric']}.")

#Creates a variable for the key and value then prints
num = favorite_numbers['tony']
print("Tony's favorite number is " + str(num) + '.')

#Use a for loop to print the key and value for the dictionary
for key, value in favorite_numbers.items():
	print(f"\nName: {key.title()}")
	print(f"Number: {value}")