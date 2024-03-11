import numpy as np


# Funckja generujaca dane dla dwoch algorytmow

def generate_random_values():
    # Generowanie danych dla capacity(pojemnosc cachu)

    # 1. Wprowadznie danych poprzez uzytkownika

    #try:
    #    capacity = int(input("Enter a capacity of algorithm:"))
    #except Exception as e:
    #   print(f"Error writting data: {str(e)}")

    # 2. Randomowe generowanie danych poprzez np.random
    capacity = np.random.randint(1, 15)
    # Wprowadznie dlugosci reference_string poprzez uzytkownika
    try:
        len_of_string = int(input("Enter a len of string:"))
    except Exception as e:
        print(f"Error writting data: {str(e)}")
    # Lista ktora zawiera reference_string
    pages = []

    for _ in range(len_of_string):
        # Generacja danych z odchgleniem standardowym
        page = np.random.normal(loc=10, scale=3)

        # Funckcja używana do ograniczania wartości zmiennej do określonego zakresu
        page = np.clip(page, 0, 30)

        # Przepisywanie wartosci do int
        page = int(round(page))
        pages.append(page)

    return capacity, pages
