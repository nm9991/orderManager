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

order_manager_ablak()
on_closing()
refresh_treeview()
add_order()
remove_order()
update_order()

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
