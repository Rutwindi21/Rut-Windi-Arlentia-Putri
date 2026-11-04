def make_album(artist_name, album_title, songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if songs:
        album['number_of_songs'] = songs
    return album

print("Masukkan informasi album (ketik 'q' kapan saja untuk keluar).")

while True:
    artist = input("Nama Artis: ")
    if artist == 'q':
        break

    title = input("Judul Album: ")
    if title == 'q':
        break

    user_album = make_album(artist, title)
    print(f"\nAlbum tercipta: {user_album}\n")