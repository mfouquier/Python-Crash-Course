#Create 10 tests 5 TRUE 5 FALSE
#Basic conditional expression.
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

#Conditional expression converting to lower case.
car = "Ford"
print("\nEvaluate regardless of case.")
print(car.lower() == "FORD".lower())

#False reading
pizza = 'hawaiian'
print("\n",pizza == 'sausage')

#False because of case mismatch.
nfl = "Saints"
print("\n The best NFL team is:")
print(nfl == 'saints')

my_truck = 'ford'
print("\n",my_truck == 'toyota')

#Test for equality and inequality with strings.
nfl = 'packers'
print("\nIs my favorite team the Packers?")
print(nfl == 'saints')

print("Is it the Saints?")
print(nfl != 'saints')

#Same thing using LOWER
nfl = 'Saints'
print("\nIs my favorite team the Saints?")
print(nfl.lower() == 'saints')
print("Is it the Packers?")
print(nfl.lower() != 'saints')

#Numerical tests >, <, >=, <=
number_1 = 5 
number_2 = 3
number_3 = 9
number_4 = 589
print("\nNumber Tests:")
print(34 > number_1)
print(number_2 >= 6)
print(number_3 < 88)
print(number_4 <= 500)

#Test using AND and OR keywords.
username = 'john'
age = 18
print("\nBoth must be true using AND keyword.")
print(username == 'matt' and age >= 18)
print(username == 'john' and age >= 18)
print(username == 'matt' and age >= 17)

print("\nOnly one needs to be true using OR keyword")
print(username == "matt" or age >= 18)
print(username == 'joe' or age < 1)

#Is the item in the list or not using IN and NOT
colors = ['red', 'black', 'blue', 'green', 'grey']
print("\nIs this shirt available in this color?")
print('yellow' in colors)
print('red' in colors)

shirt_color = 'black'
if shirt_color not in colors:
	print("\nPlease pick another color.")
else:
	print("\nGood choice.")

shirt_color = 'orange'
if shirt_color not in colors:
	print("\nPlease pick another color.")