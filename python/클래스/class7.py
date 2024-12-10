#<20241210>

#실습2. Supermarket 클래스
class Supermarket :
    instance = 0
    def __init__(self, location, name, product, customer) :
        self.__location = location
        self.__name = name
        self.__product = product
        self.__customer = customer
        Supermarket.instance += 1

    def print_location(self):
        print(f"위치: {self.__location}")
    
    def change_category(self, another_product):
        self.__product = another_product

    def show_list(self):
        print(f"파는 물건: {self.__product}")
    
    def enter_customer(self):
        self.__customer += 1

    def show_info(self):
        print  (f"가게 이름: {self.__name}\n"
                f"가게 위치 {self.__location}\n"
                f"파는 물건: {self.__product}\n"
                f"손님 수: {self.__customer}")
    
    def show_supermarket_count(self):
        print("클래스 인스턴스 개수: ", Supermarket.instance)

super = Supermarket("마포구", "마켓온", "과일", 10)
super.print_location()
super.change_category("음료")
super.show_list()
super.enter_customer()  # 고객 들어옴
super.enter_customer()
super.show_info()
super.show_supermarket_count()

