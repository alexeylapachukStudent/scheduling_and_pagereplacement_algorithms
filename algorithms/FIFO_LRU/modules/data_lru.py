from collections import OrderedDict


#
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = OrderedDict()  # Tutaj przechowuja sie strony
        self.access_time = {}
        self.current_time = 0

    # Sprawdzenie czy pamiec jest zajetaL
    def is_full(self):
        return len(self.pages) == self.capacity

    # Dzialanie algorytnu
    def page_fault(self, page, current_time=None):
        self.current_time += 1
        if page not in self.pages:  # Jezeli strony nie ma w cashu
            if self.is_full():  # Jak cash pelny
                # Szukamy najmniej stosowanej strony
                least_recently_used = min(self.access_time, key=self.access_time.get)
                del self.access_time[least_recently_used]
                del self.pages[least_recently_used]  # Usuwamy strone
            self.pages[page] = True  # Dodawanie strony w cash
            self.access_time[page] = self.current_time  # Odnowienie czasu dostepu do strony
            return True  # Zwracamy True, jezeli to page fault
        else:
            self.access_time[page] = self.current_time  # Odnowienie czasu dostepu do strony
            return False  # Zwracamy False, jezeli to nie page fault
