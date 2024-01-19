from logging import raiseExceptions

#Szerokosc glownego okna aplikacji
MAIN_WINDOW_SIZE_WIDTH = 0.8 # 80% procent ekranu glownego

#Wysokosc glownego okna aplikacji
MAIN_WINDOW_SIZE_HIGH = 0.6 # 60% procent ekranu glownego


class OknoKonfiguracja:

    def __init__(self, root):

        self.pointer_window = root

        # Ustaw rzeczywiste wartości okna
        self.szerokosc, self.wysokosc = self.odczytaj_rozmiar_wyswietlacza()

        self.ustaw_rozmiar_okna()

    def get_szerokosc(self):
        return self.szerokosc_okna

    def set_szerokosc(self, szerokosc):
        self.szerokosc_okna = szerokosc

    def get_wysokosc(self):
        return self.wysokosc_okna

    def set_wysokosc(self, wysokosc):
        self.wysokosc_okna = wysokosc

    def ustaw_minimalna_szerokosc(self, szerokosc):
        self.szerokosc_okna = max(szerokosc, self.szerokosc_okna)

    def ustaw_minimalna_wysokosc(self, wysokosc):
        self.wysokosc_okna = max(wysokosc, self.wysokosc_okna)
 
    def ustaw_rozmiar(self, szerokosc, wysokosc):
        self.szerokosc_okna = szerokosc
        self.wysokosc_okna = wysokosc

    def odczytaj_rozmiar_wyswietlacza(self):
        szerokosc_ekranu = self.pointer_window.winfo_screenwidth()
        wysokosc_ekranu = self.pointer_window.winfo_screenheight()
 
        if ( szerokosc_ekranu>0 ) and ( wysokosc_ekranu>0 ):
            return szerokosc_ekranu, wysokosc_ekranu
        else: raiseExceptions("Error with screen size")

    def ustaw_rozmiar_okna(self):
        szerokosc_okna = int(MAIN_WINDOW_SIZE_WIDTH * self.szerokosc)
        wysokosc_okna = int(MAIN_WINDOW_SIZE_HIGH * self.wysokosc)
        
        self.pointer_window.geometry(f"{szerokosc_okna}x{wysokosc_okna}")

