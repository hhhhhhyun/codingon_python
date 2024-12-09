#calss
a = dict()
a = set()

class b:
    pass

bb1 = b()
bb2 = b()
bb3 = b()

#클래스 변수
class Movie:
    title = "청설"

movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)
print()
print()

movie1.title = "위키드"
print(movie1.title)

movie1.score = "1"
print(movie1.score)
#print(movie2.score) -> movie2를 정의하지 않았기때문에 오류
print()
print()

#클래스 함수(메소드, Method)
class Movie :
    name = ''
    def print_msg(msg) :
        print(msg)
    def modify(self, movie) :
        self.name = movie
    def print_name(self) :
        print(self.name)

movie1 = Movie()
movie2 = Movie()

Movie.print_msg("print하기")

movie1.modify("프린트하기3")
movie1.print_name()
movie2.modify("프린트하기4") 
print("movie2.name", movie2.name)