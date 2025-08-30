def sprawdz_czy_palindrom(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input("podaj wyraz: ")
print(sprawdz_czy_palindrom(word))