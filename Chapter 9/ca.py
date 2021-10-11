destinations = ["Paris, France",
               "Shanghai, China",
                "Los Angeles, USA",
                "Sao Paulo, Brazil",
                "Cairo, Egypt"
               ]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
#Gets the index of the destination string
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index
#Gets the travelers location from their list at index 1 - plugs that string into function above to get the index in the locations list
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
#Takes the index from above and assigns it to a variable
test_destination_index = get_traveler_location(test_traveler)
#Prints the index of the travelers location based on our list of known destinations
#print(test_destination_index)

#Create an empty list inside the list attractions for each destination listed above
attractions = []
for destination in destinations:
	destination = []
	attractions.append(destination)
  
#Create a function to add attractions to each destination list
def add_attraction(destination, attraction):
  try: 
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)

  except ValueError:
    return print("That destination doesn't exist.")
  
    
  
add_attraction('Los Angeles, USA', ['Venice Beach',['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


def find_attractions(destination, interests):
	destination_index = get_destination_index(destination)
	attractions_in_city = attractions[destination_index]
	attractions_with_interest = []
	for sites in attractions_in_city:
		possible_attraction = sites
		attraction_tags = sites[1]
		#possible_attraction.append(sites[0])
		#attraction_tags.append(sites[1])
		
		for interest in interests:
			if interest in attraction_tags:
				attractions_with_interest.append(possible_attraction[0])
	return attractions_with_interest


def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: " 
  for site in traveler_attractions:
  	interests_string += site
  	return interests_string
  

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)