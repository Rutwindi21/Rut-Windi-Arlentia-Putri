def make_album(artist_name, album_title, songs=None):
    album = {
        'artist': artist_name, 
        'title': album_title
    }
    if songs:
        album['number_of_songs'] = songs
    return album

# Membuat tiga kamus album berbeda
album_1 = make_album("Tulus", "Manusia")
album_2 = make_album("BTS", "Love Yourself", 11) 
album_3 = make_album("Seventeen", "Face The Sun")

print(album_1)
print(album_2)
print(album_3)