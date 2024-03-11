import numpy as np

MAX_TIME = 1000  # zmienna dla zastosowania w nieskonczonej petli


# Funkcja obliczajqca wszystkie dane i znaczenia FCFS
def calculate_fcfs(arrival_time, burst_time, number_of_processes):
    # Inicjalizacja danych
    completion_time = np.zeros(number_of_processes, dtype="int")
    turn_around_time = np.zeros(number_of_processes, dtype="int")
    waiting_time = np.zeros(number_of_processes, dtype="int")

    # Wziecie pierwszego elementu dla dalzych obliczen
    min_index = np.argmin(arrival_time)

    completion_time[0] = burst_time[min_index] + arrival_time[min_index]

    # Obliczanie COMP
    for i in range(1, number_of_processes):
        completion_time[i] = max(0, completion_time[i - 1] + burst_time[i])
    # Obliczanie TAT oraz WAT
    for i in range(number_of_processes):
        turn_around_time[i] = max(0, completion_time[i] - arrival_time[i])
        waiting_time[i] = max(0, turn_around_time[i] - burst_time[i])
    # Obliczanie srendich wartosci
    average_wait_time = sum(waiting_time) / number_of_processes
    average_turn_around_time = sum(turn_around_time) / number_of_processes

    return turn_around_time, waiting_time, average_turn_around_time, average_wait_time


# Funkcja obliczajaca wszystkie dane i znaczenia SJF (NON-Preemtive)
def calculate_sjf_non(arrival_time_sjf, burst_time_sjf, processed, number_of_processes):
    completion_time_sjf = np.zeros(number_of_processes, dtype="int")
    turn_around_time_sjf = np.zeros(number_of_processes, dtype="int")
    waiting_time_sjf = np.zeros(number_of_processes, dtype="int")

    current_time = 0

    while current_time < MAX_TIME:
        min_burst = float('inf')  # wystawiam max wartosc dla dalszych obliczen
        min_index_burst = -1  # wystawiam min znaczenie dla minimalnego indeksu burst_time

        # petla w ktorej sprawdzam:
        for i in range(number_of_processes):
            # 1) czy proces juz byl zapuszczony 2) czy czas przebycia nie jest większy od czasu terazniejszego
            if not processed[i] and arrival_time_sjf[i] <= current_time and burst_time_sjf[i] < min_burst:
                # odnowienie wartosci
                min_burst = burst_time_sjf[i]
                min_index_burst = i
        # jezeli proces czeka w kolejce na wypelnienie:
        if min_index_burst == -1:
            current_time += 1
        else:

            # Obliczenia wszystkich wartosci zgondie z SJF NON-Preemtive
            completion_time_sjf[min_index_burst] = max(0, min_burst + current_time)
            turn_around_time_sjf[min_index_burst] = max(0, completion_time_sjf[min_index_burst] - arrival_time_sjf[
                min_index_burst])
            waiting_time_sjf[min_index_burst] = max(0, turn_around_time_sjf[min_index_burst] - burst_time_sjf[
                min_index_burst])

            processed[min_index_burst] = True  # po wszystkich obliczeniach zapisujemy ze proces zostal ukonczony

            # zmeniam current_ime na czas ukonczenia ostatniego procesu
            current_time += burst_time_sjf[min_index_burst]

        # jak suma wszystkich jedynek(TRUE) bedzie rownac sie ilosci procesow, wychodzimy z petli
        if sum(processed) == number_of_processes:
            break

    average_waiting_time_sjf_non = sum(waiting_time_sjf) / number_of_processes
    average_turn_around_time_sjf_non = sum(turn_around_time_sjf) / number_of_processes

    return (completion_time_sjf, waiting_time_sjf, turn_around_time_sjf, current_time,
            average_waiting_time_sjf_non, average_turn_around_time_sjf_non)


# Funkcja obliczajaca wszystkie dane i znaczenia SJF (Preemtive)
def calculate_sjf(arrival_time_sjf, burst_time_sjf, processed, number_of_processes):
    completion_time = np.zeros(number_of_processes, dtype="int")
    turn_around_time = np.zeros(number_of_processes, dtype="int")
    waiting_time = np.zeros(number_of_processes, dtype="int")
    remaining_time = burst_time_sjf.copy()

    current_time = 0

    while current_time < MAX_TIME:
        min_burst = float('inf')  # wystawiam max wartosc dla dalszych obliczen
        min_index_burst = -1  # wystawiam min znaczenie dla minimalnego indeksu burst_time

        # petla w ktorej sprawdzam:
        for i in range(number_of_processes):
            # 1) czy proces juz byl zapuszczony 2) czy czas przebycia nie jest większy od czasu terazniejszego
            if not processed[i] and arrival_time_sjf[i] <= current_time and burst_time_sjf[i] < min_burst:
                # odnowienie wartosci
                min_burst = burst_time_sjf[i]
                min_index_burst = i
        # jezeli proces czeka w kolejce na wypelnienie:
        if min_index_burst == -1:
            current_time += 1
        else:
            # Po wykonaniu jednego taktu procesora:
            remaining_time[min_index_burst] -= 1

            # Po skonczeniu
            if remaining_time[min_index_burst] == 0:
                completion_time[min_index_burst] = max(0, current_time + 1)
                turn_around_time[min_index_burst] = max(0, completion_time[min_index_burst] - arrival_time_sjf[
                    min_index_burst])
                waiting_time[min_index_burst] = max(0, turn_around_time[min_index_burst] - burst_time_sjf[min_index_burst])
                processed[min_index_burst] = True  # po wszystkich obliczeniach zapisujemy ze proces zostal ukonczony

            current_time += 1

        # jak suma wszystkich jedynek(TRUE) bedzie rownac sie ilosci procesow, wychodzimy z petli
        if sum(processed) == number_of_processes:
            break

    average_waiting_time_sjf = sum(waiting_time) / number_of_processes
    average_turn_around_time_sjf = sum(turn_around_time) / number_of_processes

    return (completion_time, waiting_time, turn_around_time, current_time,
            average_waiting_time_sjf, average_turn_around_time_sjf)
