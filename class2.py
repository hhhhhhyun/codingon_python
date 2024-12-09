#생성자(Constructor)
class Movie:
    def __init__(self): #메서드 이름은 __init__(언더바 두개)로 지정한다.
        print("Hello")

movie = Movie()

class Movie:
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience

movie1 = Movie("청설", 100)
movie2 = Movie("청설", 200)

print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)
print()
#
class Movie:
    def __init__(self): #메서드 이름은 __init__(언더바 두개)로 지정한다.
        print("Hello")

movie = Movie()

class Movie:
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience

movie1 = Movie("청설", 100)
print(Movie.count) #값에 영향을 미쳐 모든 값이 바뀐다.
movie2 = Movie("청설", 200)

print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count +=1
print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count +=1
print(movie1.count)
print(movie2.count)
print(Movie.count)



