from tkinter import *
from tkinter import messagebox
import password
from login_connection import *
import fo_ablak


def belepes_ablak():
    def ok_gomb_kezelese():
        if fhsz.get() == "" or fjsz.get() == "":
            messagebox.showerror("Hiba", "Nem lehet üres egyik mező sem!")
        else:
            if ab_jelszokeres(fhsz.get(), fjsz.get()) == "":
                messagebox.showerror("Hiba", "Nincs regisztrálva vagy nem jó a jelszó.")
            else:
                messagebox.showinfo("Belépés", "Üdv a fedélzeten!")
                belepes.destroy()
                fo_ablak.order_manager_ablak()

    def reg_gomb_kezelese():
        belepes.destroy()
        reg_ablak()

    belepes = Tk()
    belepes.title("Belépés")

    felh_nev_cimke = Label(belepes, text="Felhasználó neve (email):")
    felh_jelszo_cimke = Label(belepes, text="Jelszó:")

    fhsz = StringVar()
    fhsz.set("")
    felh_nev = Entry(belepes, textvariable=fhsz, width=30)
    fjsz = StringVar()
    fjsz.set("")
    felh_jelszo = Entry(belepes, textvariable=fjsz, width=20)

    gomb_ok = Button(belepes, text="OK", command=ok_gomb_kezelese, width=10)
    gomb_reg = Button(belepes, text="Regisztráció", command=reg_gomb_kezelese)

    felh_nev_cimke.grid(row=0, column=0, pady=20, padx=10, sticky=E)
    felh_jelszo_cimke.grid(row=1, column=0, padx=10, sticky=E)
    felh_nev.grid(row=0, column=1, padx=10, sticky=W)
    felh_jelszo.grid(row=1, column=1, padx=10, sticky=W)
    gomb_ok.grid(row=2, column=1, pady=20)
    gomb_reg.grid(row=2, column=0)

    belepes.mainloop()


def reg_ablak():
    def ok_gomb_kezelese():
        if jsz.get() != jsz2.get():
            messagebox.showerror("Hiba", "Nem egyforma a két beírt jelszó!")
        elif jsz.get() == "" or jsz2.get() == "" or fhnev.get() == "":
            messagebox.showerror("Hiba", "Nem lehet üres mező az ablakban!")
        else:
            ab_rogzites(fhnev.get(), jsz.get())
            regisztracio.destroy()
            belepes_ablak()

    def jelszo_gen_gomb_kezelese():
        pw.jelszo_generalasa()
        # print(pw.jelszo)
        jsz.set(pw.jelszo)
        jsz2.set(pw.jelszo)
        # regisztracio.destroy()

    regisztracio = Tk()
    regisztracio.title("Regisztráció")

    pw = password.Jelszo()

    felh_nev_cimke = Label(regisztracio, text="Felhasználó neve (email):")
    felh_jelszo_cimke = Label(regisztracio, text="Jelszó:")
    felh_jelszo_ismet_cimke = Label(regisztracio, text="Jelszó ismét:")

    fhnev = StringVar()
    fhnev.set("")

    felh_nev = Entry(regisztracio, textvariable=fhnev, width=30)
    jsz = StringVar()
    # jsz.set("")
    felh_jelszo = Entry(regisztracio, textvariable=jsz, width=20)
    jsz2 = StringVar()
    felh_jelszo_ismet = Entry(regisztracio, textvariable=jsz2, width=20)

    gomb_ok = Button(regisztracio, text="OK", command=ok_gomb_kezelese, width=10)
    gomb_jelszo_gen = Button(regisztracio, text="Jelszó generálás", command=jelszo_gen_gomb_kezelese)

    felh_nev_cimke.grid(row=0, column=0, pady=20, padx=10, sticky=E)
    felh_jelszo_cimke.grid(row=1, column=0, padx=10, sticky=E)
    felh_jelszo_ismet_cimke.grid(row=2, column=0, padx=10, sticky=E)
    felh_nev.grid(row=0, column=1, padx=10, sticky=W)
    felh_jelszo.grid(row=1, column=1, padx=10, sticky=W)
    felh_jelszo_ismet.grid(row=2, column=1, padx=10, sticky=W)
    gomb_ok.grid(row=3, column=1, pady=20)
    gomb_jelszo_gen.grid(row=1, column=2)

    regisztracio.mainloop()


ab_letrehoz()
belepes_ablak()
ab_bezar()