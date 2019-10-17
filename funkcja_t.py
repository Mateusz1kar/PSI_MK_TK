def funckja_t(text="", letter=''):
    for i in range(len(text)):
        if text[i]==letter:
            text[i]=' '
    return text


print(funckja_t(text="ala ma kota", letter='a'))