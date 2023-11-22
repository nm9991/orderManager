import sqlite3

kapcsolat = None
ab = None


def ab_letrehoz():
    global kapcsolat, ab
    kapcsolat = sqlite3.connect("DB/felhasznalok.db")
    ab = kapcsolat.cursor()
    ab.execute("CREATE TABLE IF NOT EXISTS felhasznalok (email TEXT, jelszo TEXT)")


def ab_rogzites(email, jelszo):
    global kapcsolat, ab
    ab.execute("INSERT INTO felhasznalok VALUES (?, ?)", (email, jelszo))
    kapcsolat.commit()


def ab_bezar():
    global kapcsolat, ab
    ab.close()
    kapcsolat.close()


def ab_jelszokeres(email, jelszo_input):
    jelszo = ""
    ab.execute("SELECT * FROM felhasznalok WHERE email = ? AND jelszo = ?", (email, jelszo_input))
    dolgozok = ab.fetchall()
    for rekord in dolgozok:
        if rekord[0] == email:
            jelszo = rekord[1]
    return jelszo


def ab_dupla_felhasznalo(felh):
    ab.execute("SELECT * FROM felhasznalok WHERE email = ?", (felh,))
    talalat = ab.fetchall()
    for record in talalat:
        if record[0] == felh:
            return True
        else:
            return False
