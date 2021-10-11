#Create a tuple and print the items.
buffet_items = ('pasta', 'meatballs', 'cake', 'ice cream', 'tacos')
print("Buffet Menu:")
for item in buffet_items:
	print(item.title())

#Try to change an item in the tuple - should receive an error.
#buffet_items[0] = 'kabobs'

#Create a new tuple that updates the menu and print the new menu.
buffet_items = ('hamburgers', 'meatballs', 'bbq', 'ice cream', 'tacos')
print("\nNew and Improved Menu:")
for item in buffet_items:
	print(item.title())