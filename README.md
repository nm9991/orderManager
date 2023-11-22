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

belepes_ablak()
ok_gomb_kezelese()
reg_gomb_kezelese()
reg_ablak()
ok_gomb_kezelese()
jelszo_gen_gomb_kezelese()
visszalepes()

### login_connection.py

ab_letrehoz()
ab_rogzites(...)
ab_bezar()
ab_jelszokeres(...)

### password.py

jelszo_generalasa(...)

### record_class.py

print_to_console(...)
