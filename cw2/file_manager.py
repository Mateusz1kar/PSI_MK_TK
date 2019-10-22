#zad8
#    Stwórz nowy moduł w projekcie o nazwie file_manager. Stwórz klasę FileManager z parametrem w konstruktorze file_name.
#    Klasa będzie zawierać dwie metody: read_file oraz update_file. Funkcja update_file powinna zawierac parametr text_data,
#    które w efekcie ma być dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.

class FileManager():

    def read_file(text_data=""):
        wynik=""
        try:
            file = open(text_data,"r",encoding="utf-8")
            wynik = (file.read())
            file.close()
        except Exception as e:
            print(e)
        print( wynik)


    def update_file( text_data , text):
        try:
            with open(text_data, 'a', encoding='utf-8') as file_reader:
                file_reader.write(text)
        except Exception as e:
            print(e)

#file_manager=  FileManager
#file_manager.read_file("zad9.txt")
#file_manager.update_file("zad9.txt","i oboje się kochają \n")
#file_manager.read_file("zad9.txt")