import numpy as np
from modules.generator import generate_random_values


# Funkcja zawierajaca dane algorytmu FCFS
def get_data_fcfs():
    number_of_processes, arrival_time, burst_time = generate_random_values()
    # Sortowanie wedlud indeksow
    sorted_indices = np.argsort(arrival_time)
    arrival_time = arrival_time[sorted_indices]
    burst_time = burst_time[sorted_indices]
    return arrival_time, burst_time, number_of_processes, sorted_indices


# Funckja zawierajaca dane algorytmu SJF (NON-preemtive)
def get_data_sjf_non():
    number_of_processes, arrival_time_sjf_non, burst_time_sjf_non = generate_random_values()
    processed_sjf_non = np.zeros(number_of_processes, dtype="bool")

    return arrival_time_sjf_non, burst_time_sjf_non, processed_sjf_non, number_of_processes


# Funckja zawierajaca dane algorytmu SJF (Preemtive)
def get_data_sjf():
    number_of_processes, arrival_time_sjf, burst_time_sjf = generate_random_values()
    processed_sjf = np.zeros(number_of_processes, dtype="bool")

    return arrival_time_sjf, burst_time_sjf, processed_sjf, number_of_processes
