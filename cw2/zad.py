
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

#    Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza na Fahrenheit, Rankine, Kelvin. Typ konwersji powinien być przekazany w parametrze temperature_type i uwzględniać błędne wartości.
#    Stwórz klasę Calculator, która będzie posiadać funkcje add, difference, multiply, divide.
#    Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i dodaj dodatkowe funkcje np. potęgowanie.
#    Stwórz funkcję, która wypisuje podany tekst od tyłu np. koteł -> łetok.
#    Stwórz nowy moduł w projekcie o nazwie file_manager. Stwórz klasę FileManager z parametrem w konstruktorze file_name. Klasa będzie zawierać dwie metody: read_file oraz update_file. Funkcja update_file powinna zawierac parametr text_data, które w efekcie ma być dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.
#    Zaimportuj klasę FileManager w innym pliku, a następnie zademonstruj działanie klasy.
#    W folderze projektu stwórz nowy virtualenv, a następnie zainstaluj moduł: https://github.com/yougov/chucknorris. Stwórz nowy moduł chuck_norris w swoim projekcie i stwórz funkcję która podłączy się pod ściągnięty moduł.

