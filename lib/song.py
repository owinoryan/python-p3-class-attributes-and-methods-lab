
class Song:
    pass
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Incrementing  the song count
        Song.add_song_to_count()
        
        # Addding the genre and artist to their respective lists
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        
        # Incrementing the genre and artist counts
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
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
# // Testing the Code
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)    
print(ninety_nine_problems.artist)  
print(ninety_nine_problems.genre)   
song2 = Song("Song 2", "Artist 1", "Rock")
song3 = Song("Song 3", "Jay-Z", "Rap")
song4 = Song("Song 4", "Artist 2", "Country")
song5 = Song("Song 5", "Artist 1", "Rock")
print(Song.count)                 
print(Song.genres)                 
print(Song.artists)                
print(Song.genre_count)           
print(Song.artist_count) 