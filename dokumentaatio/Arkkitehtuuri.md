# Arkkitehtuurikuvaus
## Rakenne
Rakenne noudattaa kerrosarkkitehtuuria
![Arkkitehtuuri](https://user-images.githubusercontent.com/80783887/117005417-e8555600-acef-11eb-8dc1-76fc6185da9a.png)

Hakemisto `repositories` vastaa tiedon tallennuksesta tietokantaan sekä csv-tiedostoihin, `services` vastaa sovelluslogiikasta ja `ui` käyttöliittymästä. Hakemisto `entities` sisältää luokkia ohjelman muuttujille.
## Tietojen tallennus
Hakemiston `repositories` luokat vastaavat tietojen tallentamisesta. Luokka [UserRepository](../src/repositories/user_repository.py) tallentaa käyttäjätunnuksiin liittyvän datan SQLite-tietokantaan. Tietokannassa on taulu `users`, johon tunnus tallennetaan `käyttäjätunnus | salasana` pareina. Luokka [CsvRepository](../src/repositories/csv_repository.py) vastaa csv-tiedostojen perustoiminnallisuuksiasta, kuten tiedoston luomisesta ja tyhjentämisestä. Luokat [NoteRepository](../src/repositories/note_repository.py) ja [CourseRepository](../src/repositories/course_repository.py) tallentavat tiedon kurssisuorituksista ja muistiinpanoista omiin csv-tiedostoihinsa hyödyntäen [CsvRepository](../src/repositories/csv_repository.py) -luokkaa 
## Sovelluslogiikka
Loogisen tietomallin muodostavat luokat [User](../src/repositories/user_repository.py), [Note](../src/repositories/note_repository.py) ja [Course](../src/repositories/course_repository.py)
![Entities](https://user-images.githubusercontent.com/80783887/118409704-7fc58c00-b694-11eb-915e-63cb86281fcd.png)

Sovelluslogiikan toiminnallisuudesta vastaa luokka [TrackerService](../src/services/tracker_service.py). 
Luokan metodeja ovat esimerkiksi seuraavat:
- Käyttäjän kirjautuminen:
  - `login(username, password)`, `logout`
- Uusien User-, Note- ja Course-olioiden luominen:
  - `create_user`, `create_note`, `create_course`
- Tietojen hakeminen:
  - `get_users`, `get_notes`, `get_courses`
- Tietojen poistaminen:
  - `delete_note`, `delete_course`
 
Käyttöliittymä kutsuu luokan [TrackerService](../src/services/tracker_service.py)-metodeja, joka käsittelee hakemiston `repositories` luokkia, sekä palauttaa tiedon takaisin käyttöliittymään. 
## Käyttöliittymä

Käyttöliittymä sisältää viisi erillistä näkymää:

- [Kirjautuminen](../src/ui/login_view.py)
- [Käyttäjän luominen](../src/ui/create_view.py)
- [Tervetuloa-näkymä](../src/ui/user_view.py), jossa myös lista suorituksista ja muistiinpanoista
- [Suorituksen lisäys ja poisto](../src/ui/add_course_view.py)
- [Muistiinpanon lisäys ja poisto](../src/ui/add_note_view.py)

Näkymät ovat erillisiä luokkia, joiden väliset yhteydet on toteutettu [UI](../src/ui/ui.py)-luokkana. Näkymät kutsuvat TrackerServicen metodeja.
## Toiminnallisuudet
### Kirjautuminen
Kirjautumisnäkymän kenttiin syötetään käyttäjätunnus ja salasana, jonka jälkeen "Kirjaudu"-painike käynniostää tapahtumankäsittelijän.

![Kirjautuminen](https://user-images.githubusercontent.com/80783887/115996379-a3db0380-a5e7-11eb-829f-104a34221397.png)

Sovelluslogiikan "login" metodi kutsuu käyttäjärepositiota, joka tarkastaa käyttäjätietokannasta, ovatko tunnus ja salasana oikein. 
### Suorituksen lisääminen
![Kurssisuoritukset lisääminen](https://user-images.githubusercontent.com/80783887/117972023-4955dd00-b333-11eb-9da7-a57786fc31ab.png)

Sovelluslogiikan "create_course" metodi luo Course-olion ja kutsuu kurssirepositoriota, joka tallentaa kurssin tiedot tiedostoon. Käyttöliittymä palaa takaisin aloitusnäkymään, jossa on lista lisätyistä kursseista. Käyttöliittymä nostaa virheilmoitukset, jos arvosana tai opintopisteet on annettu kirjaimin tai negatiivinen luku.
### Muistiinpanon lisääminen
![Muistiinpanon lisääminen](https://user-images.githubusercontent.com/80783887/118113883-867fa500-b3ef-11eb-8835-1b61c4bedfce.png)

Sovelluslogiikan "create_note" metodi luo uuden Note-olion ja kutsuu muistiinpanorepositoriota, joka tallentaa muistiinpanon tiedostoon. Käyttöliittymä antaa virheilmoituksen, jos käyttäjä ei täytä kaikkia pyydettyjä tietoja.

