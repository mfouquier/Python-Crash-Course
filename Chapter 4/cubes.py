#Print the cube of numbers 1 - 10 using a FOR loop.
cubes = []

for value in range(1, 11):
	cube = value ** 3
	cubes.append(cube)

print(cubes)

#Same loop in a shorter way.
cubes = []

for value in range(1, 11):
	cubes.append(value **3)

print(cubes)

#List Comprehension that does the same thing.
cubes = [value **3 for value in range(1, 11)]

for cube in cubes:
	print(cube)