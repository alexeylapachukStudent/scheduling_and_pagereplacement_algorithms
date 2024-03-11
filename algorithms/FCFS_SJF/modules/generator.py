import numpy as np


# Niektore rzeczy zostaly zakomentowane dla wyboru kilku opcji generowania danych


# Funkcja generujaca randomowe wartosci/wprowazdone
def generate_random_values():
    # Generowanie randomowej ilosci procesow

    # 1. Wprowadzenie ilosci danych
    # number_of_processes = int(input("Enter number of processes:"))

    # 2. Za pomoca np.random
    number_of_processes = np.random.randint(1,25)
    # Inicjalizacja list
    processes_arrival_time = np.array([], dtype="int")
    processes_burst_time = np.array([], dtype="int")
    unique_times = set()

    for _ in range(number_of_processes):
        while True:
            # Randomowa generacja arrival_time(czasu przebycia)
            arrival_time = np.random.randint(0, number_of_processes * 3)  # Zamiast 3 moze byc dowolna liczba
            # Drugi sposob generowania danych przebycia(arrival_time)

            # arrival_time = np.random.normal(loc=4, scale=10)
            # arrival_time = np.clip(arrival_time, 1, 15)
            # arrival_time = int(round(arrival_time))

            # Wybor wartosci ktorych nie ma w slowniku(unikalne wartosci)
            if arrival_time not in unique_times:
                # Randomowa generacja burst_time(czasu wykonania)

                # burst_time = np.random.randint(5, 6)

                # Drugi sposob generowania danych wykonania(burst_time)

                burst_time = np.random.normal(loc=10, scale=4)

                # Maksymalna wartosc ktora moze przyjmowac burst_time = 100
                burst_time = np.clip(burst_time, 1, 100)
                burst_time = int(round(burst_time))

                unique_times.add(arrival_time)

                processes_arrival_time = np.append(processes_arrival_time, arrival_time)
                processes_burst_time = np.append(processes_burst_time, burst_time)
                break

    return number_of_processes, processes_arrival_time, processes_burst_time
