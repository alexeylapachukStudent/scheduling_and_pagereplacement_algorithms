from modules.collecting_results import collection_info
from openpyxl import Workbook


# Funckja ktora tworzy i zapisuje nowe dane do Excela
def save_to_excel_common(algorithm, pages, page_faults, page_hits, hit_ratio, fault_ratio):
    # Wybor drogi do pliku

    if algorithm == "FIFO":
        path = r"logs_fifo.xlsx"
    else:
        path = r"logs_lru.xlsx"

    # Tworzenie ksiazki
    wb = Workbook()

    ws = wb.active

    # Umieśćamy dane w arkuszu
    data = [
        ["Page", "Page Fault", "Page Hit"],
        *[[page, "Yes" if page_faults[i] else "No", "Yes" if page_hits[i] else "No"] for i, page in
          enumerate(pages)],
        [""],
        ["Hit Ratio", " ", "Fault ratio"],
        [f"{round(hit_ratio, 2)}%", " ", f"{round(fault_ratio, 2)}%"]

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

# Funckja ktora tworzy i zapisuje nowe dane do Excela
def save_fifo():
    capacity, pages, page_faults, page_hits, hit_ratio, fault_ratio = collection_info("FIFO")
    save_to_excel_common("FIFO", pages, page_faults, page_hits, hit_ratio, fault_ratio)

# Funckja ktora tworzy i zapisuje nowe dane do Excela
def save_lru():
    capacity, pages, page_faults, page_hits, hit_ratio, fault_ratio = collection_info("LRU")
    save_to_excel_common("LRU", pages, page_faults, page_hits, hit_ratio, fault_ratio)
