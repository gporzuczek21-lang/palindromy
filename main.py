def sprawdz_czy_palindrom(word):
    return word == word[::-1]    

word = input("podaj wyraz: ")
print(sprawdz_czy_palindrom(word))