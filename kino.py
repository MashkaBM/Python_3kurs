
#Задача 1 "Кино"

class Human:
    def __init__(self, name: str, sex: str, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
        
class Movie:
    def __init__(self, name: str, director: str, year, country: str, duration, age_rating):
        self.name = name
        self.director = director
        self.year = year
        self.country = country
        self.duration = duration
        self.age_rating = age_rating
    def is_allowed(self, human):
        allowding = self.age_rating <= (2022-(human.year_of_birth))
        return allowding

class Cartoon(Movie):
    def __init__(self, name: str, director: str, year, country: str, duration, age_rating, technique: str):
        self.technique = technique

class Anime(Cartoon):
    def __init__(self, name: str, director: str, year, country: str, duration, age_rating, technique: str):
        self.technique = 'Рисованный'
        self.country = 'Япония'


movie = Movie(
  name="Dune", director="Denis Villeneuve", year=2021,
  country="USA", duration=155, age_rating=13
)
human = Human(name="Neo", sex="M", year_of_birth=1964)

print(movie.is_allowed(human))