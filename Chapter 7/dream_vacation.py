dream_vacation = {}

active = True

while active:
	name = input("What is your name? ")
	vaca_spot = input("Where is your drema vacation spot? ")
	
	dream_vacation[name] = vaca_spot

	repeat = input("Would anyone else like to answer?  yes/no: ")

	if repeat == 'no':
		active = False

for name, vaca_spot in dream_vacation.items():
	print(f"\n{name.title()} would love to go to {vaca_spot.title()}.")
	