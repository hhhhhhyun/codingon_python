#접근제어
class Movie:
    count = 0

    def __init__(self, title, audience):
        self.__title = title #title은 나만 접근 가능한 것
        self._audience = audience
        Movie.count += 1

    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self._title = title

    def get_audience(self) :
        return self._audience

movie1 = Movie("청설", 100)
print(movie1.get_title())
print(movie1._audience)
print(movie1.get_audience())

# 실습0
class MyAdd :
    __a = 1
    __b = 2

    def sum(self):
        return self .__a + self .__b
    def set_a(self, a):
        self.__a = a

a = MyAdd()
print(a.sum())
a.set_a(3)
print(a.sum())