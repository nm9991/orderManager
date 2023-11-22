class Felhasznalo:
    pass


class Jelszo:
    jelszo = 'sf'

    def __init__(self):
        self.jelszo_generalasa()

    def jelszo_bekerese(self):
        pass

    def jelszo_ellenorzese(self):
        pass

    def jelszo_generalasa(self, hany_betu_legyen = 10, kisbetu_bool = True, nagybetu_bool = True, szam_bool = True):
        import string
        import random
        password = ""
        karaktersor = ""
        if kisbetu_bool:
            karaktersor = karaktersor + string.ascii_lowercase
        if nagybetu_bool:
            karaktersor = karaktersor + string.ascii_uppercase
        if szam_bool:
            karaktersor = karaktersor + string.digits

        for _ in range(hany_betu_legyen):
            password = password + karaktersor[random.randint(0, len(karaktersor) - 1)]

        self.jelszo = password


if __name__ == "__main__":
    pw = Jelszo()
    print(pw.jelszo)