Program leírása:

Alap koncepció: 3 féle feladatkör létezik (Admin, Banki dolgozó és ügyfél)
Mindhárom más-más metódusokat jogosult meghívni.
A main.py filet futtatva, egy "bejelentkező" mező nyílik meg.
Itt a 3 típus küzöl szükséges választani, az első személyek belépési adatai:
Admin: ladamtla, 123
Dolgozó: test, 123
Ügyfél: test, 123

Az admin jogusultságai: Dolgozó létrehozása, admin létrehozása, dolgozó adatmódosítása, saját adatok módosítása
A dolgozó jogosultságai: Ügyfél létrehozása, ügyfél adatmódosítása, ügyfél adatlekérdezés, saját adatok módosítása
Ügyfél jogusultságai: Átutalás másik ügyfélnek, saját adatok megtekintése, korábbi tranzakciók listázása

A program teljes egésze úgy lett megírva, hogy minden adat mentésre kerül csv fájlokba, és objektumként is lérejön, rögtön, valamint következő indításkor betöltődik.
A program igyekszik betartani az OOP szabályokat.
A program jelenlegi formályában, terjedelmében teljesen működőképes.



---
Feladatmegosztás: kb. 50-50%

* = közös

Enikő:
    - person
    - employee
    - customer
    - transactions
    - *exceptionhandling
    - *menu
    - *main

Ádám:
    - bankaccount
    - admin
    - updater
    - format
    - *exceptionhandling
    - *menu
    - *main


---
Keller Enikő
Lénárt Ádám Tamás
