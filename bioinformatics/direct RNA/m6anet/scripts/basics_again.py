# dictionaries - fast (use hashing), changeable, unorderd, unique key:value pairs
capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Bejing",
            "Russia":"Moscow"}
# print(capitals["Germany"])  # if not in the dict -> KeyError
print(capitals.get("Germany"))  # None if no such key
print(capitals.get("USA"))
print(capitals.keys())  # print all keys
print(capitals.values())  # all values
print(capitals.items())  # entire dict
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("China")  # remove key:value by key from dict
# capitals.clear()  # clear dict
for key,value in capitals.items():
    print(key, value)


# programowanie defensywne - wszystko o pójdzie źle - pójdzie źle, a user to idiota
# snake_case dla zmiennych
# CamelCase dla klas
# 5 (%) modulo 2 - reszta dzielenia 5/2
# 5 // 2 - wynik dzielenia zaokrągla do najbliższej całkowitej

a = 5
b = 3
print("Dzielenie:", a+b, end="")  # "" zastąpi domyslnego \n na końcu
print("Dzielenie:", a+b, sep="###")

print("aul" in "Paulo Cohelo")  # True

napis = "Ala ma kmiota"
print(napis[0])
print(napis[2:8])  # exclude last
print(napis[:8])
print(napis[2:])
print(napis[2:9:2])
print(napis[-7:-1]) # exclude last (last index is -1, so exclude last char)

print(napis.index("m"))  # print lowest index of "m" in string name
print(napis.count("m"))

print(napis.lower())
print(napis.capitalize())
print(napis.upper())

print(napis.replace(" ", "_"))

print(len(napis))

a = "John"
b = "wolnowybiegowym"
print(f"Cześć {a}. Jestem dzikiem {b}")


class Osoba:
    AGE = 0  # zmienna klasowa
    NAME = ""
    def __init__(self, imie="Default", wiek=18, zawod="nothing", money=0):  # konstruktor - specjalna metoda (fcja) wywoływana za każdym razem, gdy tworzymy obiekt a podstawie klasy
        # self - konieczny pierwszy parametr w metdach. Stosowany by metody mogly odnosic sie do obirktu na którym są wywołane
        self.name = imie
        self.age = wiek
        self.job = zawod
        self.__money = money
    def przywitaj_sie(self):
        print(f'Cześć, jestem {self.name}. Mam {self.age} lat. Jestem {self.job}em')

    def work(self, some_cash):
        self.__money += some_cash
    def get_money_status(self):
        return self.__money

osoba1 = Osoba("Mateusz", 26, "student")
osoba1.przywitaj_sie()
osoba2 = Osoba()
osoba2.przywitaj_sie()
osoba2.work(100)
print(osoba2.get_money_status())

