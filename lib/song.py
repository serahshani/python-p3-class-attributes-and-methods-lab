class Song:
    # Class variables
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance variables
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class variables
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    @classmethod
    def get_total_songs(cls):
        """Returns the total count of songs."""
        return cls.count

    @classmethod
    def get_genres(cls):
        """Returns a list of unique genres."""
        return cls.genres

    @classmethod
    def get_artists(cls):
        """Returns a list of unique artists."""
        return cls.artists

    @classmethod
    def get_genre_count(cls):
        """Returns a dictionary with the count of each genre."""
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        """Returns a dictionary with the count of each artist."""
        return cls.artist_count

# Example Usage
song1 = Song("Song One", "Artist A", "Pop")
song2 = Song("Song Two", "Artist B", "Rock")
song3 = Song("Song Three", "Artist A", "Pop")

# Accessing class methods to get information
print("Total songs:", Song.get_total_songs())
print("Genres:", Song.get_genres())
print("Artists:", Song.get_artists())
print("Genre count:", Song.get_genre_count())
print("Artist count:", Song.get_artist_count())
