#1
text = """ჯასურბეკ იახშიბოევის ქუჩაზე მცხოვრები
კურიერის შაურმის მოლოდინში ველი"""

for line in text.split("\n"):
    print(len(line.split(" ")))


#2
class Movie:
    def __init__(self, title, genre, release_year, rating=0.0):
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_release_year(self):
        return self.release_year

    def get_rating(self):
        return self.rating

    def __str__(self):
        return f"Movie title: {self.title}, Genre: {self.genre}, Release Year: {self.release_year}, Rating: {self.rating}/5"


class MovieDatabase:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_all_movies(self):
        if not self.movies:
            print("No movies in the database.")
        else:
            for movie in self.movies:
                print(movie)
