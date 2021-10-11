sandwich_orders = ['cuban', 'rueben', 'roast beef', 'turkey']
finished_sandwiches = []

#Loop through the list of sandwiches and pop them out one at a time. Then add them to the empty
#List of finished sandwiches
while sandwich_orders:
	making_sandwich = sandwich_orders.pop()
	print(f"I made your {making_sandwich.title()} sandwich")
	finished_sandwiches.append(making_sandwich)

print("\nThese sandwiches were made:")

#Print the sandwiches that were made.
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())