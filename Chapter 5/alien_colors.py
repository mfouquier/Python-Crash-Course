alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points.")

#Write a version that fails the if test.
alien_color = 'red'

if alien_color == 'green':
	print("You just earned 5 points!")

#IF ELSE statements write it twice to generate both outcomes.
alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points!")
else:
	print("You just earned 10 points!")

alien_color = 'red'

if alien_color == 'green':
	print("You just earned 5 points!")
else:
	print("You just eanred 10 points!\n")

#IF ELIF ELSE statements print all three variations.
alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points.")
elif alien_color == 'yellow':
	print("You just earned 10 points.")
elif alien_color == 'red':
	print("You just earned 15 points.")

alien_color = 'yellow'

if alien_color == 'green':
	print("You just earned 5 points.")
elif alien_color == 'yellow':
	print("You just earned 10 points.")
elif alien_color == 'red':
	print("You just earned 15 points.")

alien_color = 'red'

if alien_color == 'green':
	print("You just earned 5 points.")
elif alien_color == 'yellow':
	print("You just earned 10 points.")
elif alien_color == 'red':
	print("You just earned 15 points.\n")

#IF ELIF ELSE about age and stages of life
age = 65

if age < 2:
	print("You are a baby.")
elif age < 4:
	print("You are a toddler.")
elif age < 13:
	print("You are a kid.")
elif age < 20:
	print("You are a teenager.")
elif age < 65:
	print("You are an adult.")
elif age >= 65:
	print("You are an elder.")