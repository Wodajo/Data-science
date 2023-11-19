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