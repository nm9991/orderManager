class Record:
    ID = None
    nev = ""
    cim = ""
    rendelt_targy = ""
    mennyiseg = None

    def __init__(self, ID, nev, cim, rendelt_targy, mennyiseg):
        self.ID = ID
        self.nev = nev
        self.cim = cim
        self.rendelt_targy = rendelt_targy
        self.mennyiseg = mennyiseg

    def print_to_console(self):
        print("A rekord adatai:\n\n"
              "Rendelési azonosító:", self.ID,
              "\nNév:", self.nev,
              "\nLakcím:", self.cim,
              "\nRendelt tárgy:", self.rendelt_targy,
              "\nRendelt mennyiség:", self.mennyiseg,
              "\n---------------------")
