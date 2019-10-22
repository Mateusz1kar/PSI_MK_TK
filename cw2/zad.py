
#zad1
#   Stwórz funkcję, która jako parametry przyjmuje dwie listy a_list oraz b_list.
#   Następnie zwróć listę, która będzie posiadać parzyste indeksy z listy a_list oraz nieparzyste z b_list.
def zad1(a_list=[],b_list=[]):
    wynik=[]
    for i in range(0, max([len(a_list) , len(b_list)]) ):
        if i % 2==0:
            if i<=len(a_list):
                wynik.append(a_list[i])
        else:
            if i<=len(b_list):
                wynik.append(b_list[i])
    return wynik

print(zad1([1,2,3,4,5],[6,7,8,9]))

#  zad2
#  Stwórz funkcję, która przyjmuje parametr data_text, a następnie zwróci następujące informacje o parametrze w formie słownika (dict):
#     length: długość podanego tekstu,
#       letters: lista znaków w wyrazie np. ['D', 'o', 'g'],
#        big_letters: zamieniony parametr w kapitaliki np. DOG
#        small_letters: zamieniony parametr w małe litery np. dog
def zad2 (text=""):
    wynik=dict(lenght=len(text), letters=set(text), big_letters=text.upper(), small_letters=text.lower())
    return wynik
print(zad2("dog"))

#zad3
 #   Stwórz funkcję, która przyjmie jako parametry text oraz letter,
#   a następnie zwróci wynik usunięcia wszytkich wystąpień wartości w letter z tekstu text.
def zad3(text="",letera=''):
    wynik=text
    for i in range(0,len(letera)):
        wynik=wynik.replace(letera[i],'')

    return wynik
text ="ala ma kota"
#print(text.replace("a",""))
print(zad3(text,'al'))
#zad4
#    Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin.
#    Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać błędne wartości.

def zad4(temperature=0, temperature_type='k'):
    if temperature >= (-273.15):
        if temperature_type=="k":
            print("{}C to {}K".format(temperature,temperature+273.15 ))
        elif temperature_type=="f":
            print("{}C to {}F".format(temperature, temperature * 1.8+32))
        elif temperature_type=="r":
            print("{}C to {:.2f}R".format(temperature, (temperature  + 273.15) * 1.8))
        else:
            print("Zła warość typu temperatury")
    else:
        print("Podana temperatura nie ijstnieje najnisza temperatura to −273,15 *C")

zad4(0,"r")

#zad5
#    Stwórz klasę Calculator, która będzie posiadać funkcje add, difference, multiply, divide.

class Calculator:
    def add(self,x=0,y=0):
        return x+y
    def difference(self,x=0,y=0):
        return x-y
    def multiply(self,x=0,y=0):
        return x*y
    def divide(self,x=0,y=1):
        return x/y
#zad6
#    Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i dodaj dodatkowe funkcje np. potęgowanie.

class ScienceCalculator(Calculator):
    def exponentiation(self,x=0,y=0):
        return x**y

#zad7
#    Stwórz funkcję, która wypisuje podany tekst od tyłu np. koteł -> łetok.
def zad7(text=""):
     print(text[::-1])
zad7("koteł")







#    Zaimportuj klasę FileManager w innym pliku, a następnie zademonstruj działanie klasy.
#    W folderze projektu stwórz nowy virtualenv, a następnie zainstaluj moduł: https://github.com/yougov/chucknorris. Stwórz nowy moduł chuck_norris w swoim projekcie i stwórz funkcję która podłączy się pod ściągnięty moduł.

