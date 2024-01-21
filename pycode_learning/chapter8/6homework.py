# homework 8-6
# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the values that are returned.

def city_country(city, country):
    return city.title() + ', ' + country.title()
city = city_country('santiago', 'chile')
print(city)
city = city_country('beijing', 'china')
print(city)
city = city_country('new york', 'america')
print(city)

# homework 8-7
# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
# If the calling line includes a value for the number of songs, add that value to the album's dictionary.
# Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, number=''):
    album = {'artist': artist_name, 'album': album_title}
    if number:
        album['number'] = number
        return album
    else:
        return album
album = make_album('jay', 'jay')
print(album)
album = make_album('jay', 'jay', 10)
print(album)
album = make_album('jay', 'jay', number=10) 
print(album)

# homework 8-8

def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'album': album_title}
    return album
while True:
    print("\nPlease tell me your favorite artist and album:")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist: ")
    if artist == 'q':
        break
    album = input("Album: ")
    if album == 'q':
        break
    album = make_album(artist, album)
    print(album)
    