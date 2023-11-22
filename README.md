# Beadandó feladat: Rendeléskezelő program
## Készítette: Nagy Márk

## Feladat leírása:

A program lehetőséget biztosít új felhasználók regisztrálására.
A regisztrált felhasználók beléphetnek egy rendelések számontartására szolgáló rendszerbe.
A főablakban a rendszer táblázatosan kilistázza a rendszerben tárolt adatokat, továbbá megjeleníti a műveletekhez használatos beviteli mezőket.  
  
A rendszeren belül a felhasználók képesek:  
-Új rendelések hozzáadására  
-Meglévő rendelések módosítására  
-Meglévő rendelések törlésére  
  
A program minden művelet után frissíti a grafikus felületet.
Az ablak bezárásával a felhasználó kijelentkezhet, ekkor az adatbázissal való kommunikáció lezáródik.

## Használt modulok:
  
Tkinter  
Sqlite3  
Pillow  
+Egyéni, a programban megtalálható modulok  

## Függvények leírása:

### fo_ablak.py

order_manager_ablak(): A főablak megjelenítéséért, adatainak tárolásáért, műveleteinek definiálásáért felelős függvény.  
  
on_closing(): Eseménykezelő függvény. Az ablak bezárásakor megkérdezi a felhasználót, hogy biztos bezárja-e a programot. Ha igen, akkor lezárja az adatbázis kommunikációt.  
  
refresh_treeview(): A grafikus felület frissítéséért felelős függvény. Induláskor és műveletek után fut le.  
  
add_order(): A hozzáadás gomb lenyomásához rendelt függvény. Hozzáad egy új rekordot az adatbázishoz a mezőkbe írt adatok alapján.  
  
remove_order(): A törlés gomb lenyomásához rendelt függvény. Kitörli a megadott ID-hez tartozó rekordot az adatbázisból.  
  
update_order(): A módosítás gomb lenyomásához rendelt függvény. Módosítja a megadott ID-hez tartozó rekordot a mezőkbe írt adatok alapján.  
  

### login.py

belepes_ablak(): A bejelentkező ablak megjelenítéséért, bejelentkezésért felelős függvény. Ezen felül átirányítást is biztosít a regisztráció ablakra.  
  
belepes_gomb_kezelese(): A belépés gomb lenyomásához rendelt függvény. Megnézi, hogy a beírt adatok alapján talál-e felhasználót az adatbázisban. Ennek megfelelően reagál.  
  
reg_gomb_kezelese(): A bejelentkező ablakbeli regisztráció gomb lenyomásához rendelt függvény. Átirányítja a felhasználót a regisztráció ablakra.  
  
reg_ablak(): A regisztráció ablak megjelenítéséért, regisztrációért felelős függvény. Ezen felül visszalépési lehetőséget is biztosít a belépés ablakra, továbbá jelszó generálást is biztosít.  
  
registration_gomb_kezelese(): A regisztráció ablakbeli regisztráció gomb lenyomásához rendelt függvény. A beírt adatok alapján regisztrál egy új felhasználót az adatbázisba.  
  
jelszo_gen_gomb_kezelese(): A regisztráció ablakbeli jelszó generáló gomb lenyomásához rendelt függvény. Generál egy 10 karakter hosszú véletlenszerű jelszót a jelszó mezőkbe.  
  
visszalepes(): A regisztráció ablakbeli visszalépés gomb lenyomásához rendelt függvény. Visszalépteti a felhasználót a bejelentkező ablakra.  
  

### login_connection.py

ab_letrehoz()
ab_rogzites(...)
ab_bezar()
ab_jelszokeres(...)

### password.py

jelszo_generalasa(...)

### record_class.py

print_to_console(...)
