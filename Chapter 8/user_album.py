def make_album(artist_name, album_title, tracks=0):
	'''Returns album artist, info and an optional item Tracks to a dictionary'''
	album_info = {
	'artist':artist_name.title(), 
	'title':album_title.title(), 
	}

	if tracks:
		album_info['tracks'] = tracks
	return album_info

'''Create a WHILE loop to get user input and add it to a dictionary in the function'''
while True:
	print("Enter 'q' at any time to exit")

	band = input("What is the name of the band? ")
	if band == 'q':
		break
	album = input("What is the title of their album? ")
	if album == 'q':
	 	break

	album = make_album(band, album)
	print(album)

print("Thanks for responding!")