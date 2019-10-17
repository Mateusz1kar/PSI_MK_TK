def funkcja_d(data_text=""):
    wynik = dict(lenght=len(data_text), letters=list(data_text), big_letters=data_text.upper(), small_letters=data_text.lower())
    return wynik


print(funkcja_d(data_text="Dog"))