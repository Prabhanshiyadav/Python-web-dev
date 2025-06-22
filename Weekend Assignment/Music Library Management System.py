def add_album(library, album_info):
    artist, title, year, songs = album_info
    library[title] = (artist, year, songs)
    print(f"\n✅ Album '{title}' added successfully.")
    return library
def create_playlist(library, selections):
    playlist = []
    for album_title, song_title in selections:
        if album_title in library:
            _, _, songs = library[album_title]
            if song_title in songs:
                playlist.append(song_title)
    print("\n✅ Playlist created.")
    return playlist
def add_song_to_album(library, album_title, new_song):
    if album_title in library:
        artist, year, songs = library[album_title]
        if new_song not in songs:
            songs.append(new_song)
            library[album_title] = (artist, year, songs)
            print(f"\n✅ Song '{new_song}' added to album '{album_title}'.")
        else:
            print("⚠️ Song already exists in album.")
    else:
        print("❌ Album not found.")
    return library
def remove_song_from_playlist(playlist, song):
    if song in playlist:
        playlist.remove(song)
        print(f"\n✅ Song '{song}' removed from playlist.")
    else:
        print("❌ Song not found in playlist.")
    return playlist
def music_library_app():
    library = {}
    playlist = []
    artists = set()
    genres = set()
    while True:
        print("\n===== 🎵 Music Library Menu =====")
        print("1. Add New Album")
        print("2. Create Playlist")
        print("3. Add Song to Album")
        print("4. Remove Song from Playlist")
        print("5. View Library")
        print("6. View Playlist")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            artist = input("Enter artist name: ")
            title = input("Enter album title: ")
            year = int(input("Enter release year: "))
            genre = input("Enter genre: ")
            songs = input("Enter songs (comma-separated): ").split(',')
            songs = [s.strip() for s in songs]
            album_info = (artist, title, year, songs)
            library = add_album(library, album_info)
            artists.add(artist)
            genres.add(genre)
        elif choice == '2':
            print("\n🎧 Available Albums:")
            for album in library:
                print(f"- {album}")
            selections = []
            while True:
                album_title = input("Enter album name to pick from (or 'done' to stop): ")
                if album_title.lower() == 'done':
                    break
                song_title = input("Enter song title: ")
                selections.append((album_title, song_title))
            playlist = create_playlist(library, selections)
        elif choice == '3':
            album_title = input("Enter album title: ")
            new_song = input("Enter new song name: ")
            library = add_song_to_album(library, album_title, new_song)
        elif choice == '4':
            song = input("Enter song to remove from playlist: ")
            playlist = remove_song_from_playlist(playlist, song)
        elif choice == '5':
            print("\n📀 Current Music Library:")
            for title, (artist, year, songs) in library.items():
                print(f"\nAlbum: {title} | Artist: {artist} | Year: {year}")
                print("Songs:", ', '.join(songs))
        elif choice == '6':
            print("\n🎶 Current Playlist:")
            print(playlist)
        elif choice == '7':
            print("\n👋 Exiting Music Library. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-7.")
music_library_app()