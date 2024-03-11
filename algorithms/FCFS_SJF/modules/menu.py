from modules.file_scaning import save_to_exel_fifo, save_sjf_non, save_sjf
from datetime import date


def menu():
    print(
        f"Hello! Today is {date.today()}\nChoose what algorithm you want to start:\n1.FCFS\n2.SJF(NON-Preemtive)\n3.SJF(Preemtive)\n4.All\n")
    try:
        lang = int(input("Enter your value(From 1-4): "))
    except Exception as e:
        print(f"Your problem is {str(e)}. Try to enter a number!")
    else:
        match lang:
            case 1:
                save_to_exel_fifo()
            case 2:
                save_sjf_non()
            case 3:
                save_sjf()
            case 4:
                save_to_exel_fifo()
                save_sjf_non()
                save_sjf()
