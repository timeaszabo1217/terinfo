# Térinformatika

Jelen projekt célja Somogy vármegye területén található, Gazdasági szervezetek, kereskedelem és vendéglátás témakörhöz kapcsolódó helyiségek, épületek és létesítmények elemzése és megjelenítése QGIS segítségével.

## Feladat szöveges leírása

A projekt célja egy választott magyarországi vármegye településeinek és járásainak térinformatikai elemzése Központi Statisztikai Hivatal (KSH) adatok felhasználásával. A feladat során a településekhez további KSH adatmezők kerülnek hozzáadásra, majd ezek alapján tematikus poligon térképek készülnek. Emellett járási szinten aggregált térképet kell létrehozni. A projekt része továbbá OpenStreetMap adatokból pontréteg készítése és egy PyQGIS script megírása, amely településenként összesíti egy kategória pontjainak számát. A térképek exportálása és dokumentálása is része a feladatnak. Szorgalmi feladatként raszteres térkép generálása is végezhető.

## Követelmények

### Vetület

- Minden réteg vetülete legyen WGS 84 / Pseudo-Mercator (EPSG:3857).

### Attribútumtábla bővítése  
- További 4 KSH adatmező került hozzáadásra a választott vármegye településeihez.  
- Két adatmező két különböző év adatait tartalmazza az időbeli összehasonlításhoz.

### Települések poligon térképe  
- Elkészült a választott vármegye településeit ábrázoló poligon térkép.  
- A települések különböző színű kitöltéssel és név szerinti címkézéssel jelennek meg.

### Tematikus térképek  
- Három poligon alapú, települési szintű tematikus térkép készült a KSH adatok elemzése alapján.  
- Alkalmazásra került fokozatos és szabály alapú megjelenítés is, a szabály alapú esetében legalább három szabály definiálva.  
- Egy térképen vizsgálták az időbeli eltéréseket két különböző év adatainak felhasználásával.  
- QGIS kifejezések segítségével kiszámításra és megjelenítésre kerültek a települési értékek vármegyei összértékhez viszonyított százalékos arányai, két tizedesjegyre kerekítve.

### Járás szintű összesítő térkép  
- Egy járási szintű poligon térkép készült, amely a járásba tartozó települések egy kiválasztott adatának összesítését jeleníti meg (összeg, minimum, maximum, átlag vagy medián).  
- Az összesítési művelet dinamikusan történik a jelrendszer vagy címkézés beállításai alapján, így az adatváltozás esetén automatikusan frissül.

### Térképek exportálása  
- A 2. és 3. részfeladatoknak megfelelő térképek exportálásra kerültek a Nyomtatási elrendezés funkció segítségével, címekkel és jelmagyarázatokkal, a megadott formátumban (JPG vagy PDF).  
- A 2. részfeladathoz tartozó térképen a jelmagyarázat elhagyásra került, mivel a színezés csak a települések megkülönböztetését szolgálja.

### Pontréteg Open Street Map adatokból  
- Az OSM adatok alapján három kategóriába sorolt pontréteg készült a választott vármegyében található, a témakörhöz kapcsolódó helyiségekről/épületekről/létesítményekről.  
- Poligon alapú objektumok esetén azok súlypontját vették figyelembe a pontok meghatározásához.  
- A pontréteg vetülete WGS 84 / Pseudo-Mercator (EPSG:3857).

### PyQGIS script  
- Egy PyQGIS script készült, amely a választott vármegye települései attribútumtáblájához hozzáad egy egész szám típusú mezőt, amely az egyik kategóriába tartozó pontok számát tartalmazza településenként.  
- A pontréteg megjelenítéséhez szabály alapú megjelenítés készült, kategóriánként eltérő színnel és alakzattal.
