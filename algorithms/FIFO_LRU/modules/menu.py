from modules.tables import save_fifo, save_lru
from datetime import date


# Funckja menu
def menu():
    print(
        f"Hello! Today is {date.today()}\nChoose what page replacement algorithm you want to start:\n1.FIFO\n2.LRU\n3.All")
    try:
        lang = int(input("Enter your value(From 1-3): "))
    except ValueError:
        print("Try to enter a number!")
    else:
        match lang:
            case 1:
                save_fifo()
            case 2:
                save_lru()
            case 3:
                save_fifo()
                save_lru()

