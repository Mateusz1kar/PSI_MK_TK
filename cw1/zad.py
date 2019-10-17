zad1 = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w" \
       " przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez" \
       " nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później " \
       "zaczął być używany przemyśle elektronicznym, pozostając praktycznie" \
       " niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy " \
       "Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne" \
       " wersje Lorem Ipsum oprogramowaniem przeznaczonym " \
       "do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

imie = "Mateusz"
nazwisko = "Karcz"
litera_1 = imie[2]
litera_2 = nazwisko[3]
suma = [0,0]
for i in range(len(zad1)):
    if zad1[i] == litera_1:
        suma[0]=suma[0]+1
    elif zad1[i] == litera_2:
        suma[0]=suma[0]+1
print("W tekście jest "+str(suma[0])+" liter " +litera_1+" oraz "+ str(suma[1])+" liter "+litera_2)

#zad5
karcz="Mateusz Karcz"
print(" ".join(map(lambda s: s.capitalize(), karcz[::-1].split(" "))))

#zad6
#Stwórz listę z wartościami od 1 do 10. Następnie podziel listę tak, aby pierwsze 5
# liczb zostało w oryginalnej liście a pozostałe 5 znalazło się w nowej liście.
lista = list(range(1, 10))
nowa_lista = lista[5:]
lista = lista[:5]
print(lista, nowa_lista)

#zad7
#Połącz te listy ponownie. Dodaj do listy wartość „0” na początku.
# Utwórz kopię połączonej listy i wyświetl listę posortowaną malejąco.
merged = lista + nowa_lista
merged.insert(0, 0)
kopia_merged = merged.copy()
kopia_merged.sort(reverse=True)
print(merged)
print(kopia_merged)

#zad8
#Za pomocą krotek stwórz listę studentów swojej grupy przypisując numer indeksu do imienia i
# nazwiska (dane nie muszą być prawdziwe).
studenci=[
    ("Mateusz","Karcza",145886),
    ("Bartosz","H.",145000),
    ("Tomasz","K.",145999),
    ]
print(studenci)

#zad9
#Przekształć poprzednie zadanie na słownik, a następnie dodaj pary zawierające wiek, adres email,
# rok urodzenia oraz adres.
studenci_dict=dict({
    145886: {
        "imie": "Mateusz",
        "nazwisko": "Karcza",
        "wiek": 21,
        "adres email": "kar.mateusz@wp.pl",
        "rok uroczenia": "1997",
        "adres": "surowe 157"
    },
    145000:{
        "imie": "Bartosz",
        "nazwisko": "H.",
        "wiek": 21,
        "adres email": "h.barosz@gmail.com",
        "rok uroczenia": "1997",
        "adres": "czrna dziura"
    },
    145999:{
        "imie": "Tomasz",
        "nazwisko": "K.",
        "wiek": 21,
        "adres email": "k.tomasz@gmai.com",
        "rok uroczenia": "1997",
        "adres": "nidzica"
    }
})
print(studenci_dict)

#zad10
#Stwórz listę zawierającą numery telefonów z powtórzeniami, a następnie usuń powtórzenia za pomocą
# rzutowania na set.
numery=[999888777,888999777,999888777,665778990,888999777]
zbiur=set(numery)
print(zbiur)

#zad11
#Korzystając z funkcji range wypisz elementy rosnąco od 1 - 10
print(list(range(1,11)))

#zad12
#Korzystając z funkcji range wypisz elementy malejąco od 100 - 20, co 5 wartości.
print(list(range(100,19,-5)))