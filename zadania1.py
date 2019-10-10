zmienna = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
zmienna_typu_string = "elo"
imie = "Tomasz"
nazwisko = "Kałędkowski"
litera_1 = imie[2]
litera_2 = nazwisko[3]
licznik1 = 0
licznik2 = 0
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista[5:10]
lista = lista[0:5]
lista3 = lista + lista2
lista3.insert(0, 0)
kopia = lista3
kopia.sort()
kopia.reverse()
for i in range(len(zmienna)):
    if zmienna[i] == litera_1:
        licznik1 += 1
    if zmienna[i] == litera_2:
        licznik2 += 1
print("W tekście jest "+str(licznik1)+" liter m oraz "+str(licznik2)+" liter ę")
print(imie[::-1]+' '+nazwisko[::-1])
print(lista)
print(lista2)
print(lista3)
print(kopia)