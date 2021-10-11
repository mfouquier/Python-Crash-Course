def make_album(artist_name, album_title, tracks=0):
'''Returns album artist, info and an optional item Tracks to a dictionary'''
	album_info = {
	'artist':artist_name.title(), 
	'title':album_title.title(), 
	}

	if tracks:
		album_info['tracks'] = tracks
	return album_info

album = make_album('tito', 'wonderland')
print(album)

album = make_album('sublime', '40oz to freedom')
print(album)

album = make_album('tom petty', 'mary jane', '12')
print(album)