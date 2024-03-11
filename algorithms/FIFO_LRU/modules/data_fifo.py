# Inicjalizacja algorytmu FIFO
class Memory_FIFO:

    # Dane ktore zawiera dany algorytm

    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []
        self.pages_set = set()
        self.access_time = {}

    # Sprawdzenie czy pamiec jest zajetaL

    def is_full(self):
        return len(self.pages) == self.capacity

    # Dzialanie algorytnu
    def page_fault(self, page, current_time):
        # Sprawdzenie czy strona jest w cashu
        if page not in self.pages_set:
            if self.is_full():
                # Jezeli cach jest pelny, usuwamy pierwsza strone
                removed_page = self.pages[0]
                self.pages.pop(0)
                self.pages_set.remove(removed_page)
                # Zmieniamy czas dostepu(usuwamy)
                del self.access_time[removed_page]

            # Jezeli strony nie ma w cash, to dodajemy ja
            self.pages.append(page)
            self.pages_set.add(page)
            self.access_time[page] = current_time  # Odnowienie czasu dostepu do strony
            # Zwracamy True, jezeli to page fault
            return True
        else:
            self.access_time[page] = current_time
            # Zwracamy False, jezeli to nie page fault
            return False
