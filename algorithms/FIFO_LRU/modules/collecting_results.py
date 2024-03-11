from modules.data_fifo import Memory_FIFO
from modules.data_lru import LRU
from modules.generator import generate_random_values


# Funkcja zbierajaca wszystkie dane
def collection_info(algorithm):
    capacity, pages = generate_random_values()
    # Wybór algorytmu
    if algorithm == "FIFO":
        page_replacement = Memory_FIFO(capacity)
    else:
        page_replacement = LRU(capacity)

    # Inicjalizacja dwoch list zawierajacych dane o hitach i faultsach

    page_fault = [0] * len(pages)
    page_hits = [0] * len(pages)

    # Petla ktora sprawdza czy nastapil fault czy hit

    for i, page in enumerate(pages):
        if page_replacement.page_fault(page, i):
            page_fault[i] += 1
        else:
            page_hits[i] += 1

    # Obliczenia prawdopodobienstwa wystapienia hits

    hit_ratio = (sum(page_hits) / len(pages)) * 100
    fault_ratio = (sum(page_fault) / len(pages)) * 100
    return capacity, pages, page_fault, page_hits, hit_ratio, fault_ratio
