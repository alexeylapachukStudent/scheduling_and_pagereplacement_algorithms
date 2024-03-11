from modules.data import get_data_fcfs, get_data_sjf_non, get_data_sjf
from modules.calculating_all_the_values import calculate_fcfs, calculate_sjf_non, calculate_sjf
from openpyxl import Workbook


def save_to_exel_fifo():
    arrival_time, burst_time, number_of_processes, sorted_indices = get_data_fcfs()
    turn_around_time, waiting_time, average_turn_around_time, average_wait_time = calculate_fcfs(arrival_time,
                                                                                                 burst_time,
                                                                                                 number_of_processes)

    path = "logs_fcfs.xlsx"  # Droga do pliku

    wb = Workbook()  # Tworzymy ksiazke
    ws = wb.active

    # Umieśćamy dane w arkuszu
    data = [
        ["Process", "Arrival Time", "Burst Time", "Turn Around Time", "Waiting Time"],
        *[[f"P{sorted_indices[i]}", arrival_time[i], burst_time[i], turn_around_time[i], waiting_time[i]] for i in
          range(number_of_processes)],
        ["Average Turn Around Time", " ", "Average Waiting Time"],
        [average_turn_around_time, " ", average_wait_time]
    ]
    # Dodawanie danych do ksiazki
    for row in data:
        ws.append(row)

    # Sprawdzenie czy dane zostaly zachowane

    try:
        wb.save(path)
        print("Data has been successfully saved to Excel!")
    except Exception as e:  # Przechwycenie dowolnego bledu
        print(f"Error saving data: {str(e)}")


def save_to_exel_sjf_common(algorithm, number_of_processes, arrival_time, burst_time, turn_around_time, waiting_time,
                            average_turn_around_time, average_wait_time):
    if algorithm == "SJF-Non":
        path = "logs_sjf_non.xlsx"
    else:
        path = "logs_sjf.xlsx"
    # Tworzymy ksiazke
    wb = Workbook()
    ws = wb.active

    # Umieśćamy dane w arkuszu
    data = [
        ["Process", "Arrival Time", "Burst Time", "Turn Around Time", "Waiting Time"],
        *[[i, arrival_time[i], burst_time[i], turn_around_time[i], waiting_time[i]] for i in
          range(number_of_processes)],
        ["Average Turn Around Time", " ", "Average Waiting Time"],
        [average_turn_around_time, " ", average_wait_time]
    ]

    # Dodawanie danych do ksiazki
    for row in data:
        ws.append(row)

    # Sprawdzenie czy dane zostaly zachowane

    try:
        wb.save(path)
        print(f"Data for {algorithm} has been successfully saved to Excel!")
    except Exception as e:
        print(f"Error saving data: {str(e)}")


def save_sjf_non():
    arrival_time_sjf_non, burst_time_sjf_non, processed, number_of_processes = get_data_sjf()
    completion_time_sjf_non, waiting_time_sjf_non, turn_around_time_sjf_non, current_time, average_waiting_time_sjf_non, average_turn_around_time_sjf_non = calculate_sjf_non(
        arrival_time_sjf_non, burst_time_sjf_non, processed, number_of_processes)

    save_to_exel_sjf_common("SJF-Non", number_of_processes, arrival_time_sjf_non, burst_time_sjf_non,
                            turn_around_time_sjf_non, waiting_time_sjf_non, average_turn_around_time_sjf_non,
                            average_waiting_time_sjf_non)


def save_sjf():
    arrival_time_sjf_non, burst_time_sjf_non, processed, number_of_processes = get_data_sjf_non()
    completion_time_sjf_non, waiting_time_sjf_non, turn_around_time_sjf_non, current_time, average_waiting_time_sjf_non, average_turn_around_time_sjf_non = calculate_sjf(
        arrival_time_sjf_non, burst_time_sjf_non, processed, number_of_processes)

    save_to_exel_sjf_common("SJF", number_of_processes, arrival_time_sjf_non, burst_time_sjf_non,
                            turn_around_time_sjf_non, waiting_time_sjf_non, average_turn_around_time_sjf_non,
                            average_waiting_time_sjf_non)
