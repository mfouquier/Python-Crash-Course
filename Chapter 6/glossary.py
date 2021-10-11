python_terms = {
	'tuple':'list that cannot be changed',
	'for_loop': 'loops through a list performing the function',
	'if': 'if this is true then perform an action',
	'elif': 'else if, if the first was false and this is true then do the action',
	'dictionary': 'collection of key-value pairs',
	'sorted': 'list items in alphabetical order',
	'string': 'a series of characters',
	'comment': 'a note in a program that the Python interpreter ignores',
}

print('Tuple - ' + python_terms['tuple'] + '.')
print(f"For_Loop - {python_terms['for_loop']}.")
print('If - ' + python_terms['if'] + '.')
print('Elif - ' + python_terms['elif'] + '.')
print(f"Dictionary - {python_terms['dictionary']}.")


#Solution from the book creates a variable from the key 

word = 'tuple'
print("\n" + word.title() + ": " + python_terms[word])

word = 'for_loop'
print("\n" + word.title() + ": " + python_terms[word])

#Print the glossary using a FOR loop 

for term, definition in python_terms.items():
	print("\n" + term + ": " + definition)