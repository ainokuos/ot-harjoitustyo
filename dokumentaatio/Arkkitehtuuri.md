# Arkkitehtuurikuvaus
## Rakenne
Rakenne noudattaa kerrosarkkitehtuuria
![Arkkitehtuuri](https://user-images.githubusercontent.com/80783887/117005417-e8555600-acef-11eb-8dc1-76fc6185da9a.png)

Hakemisto `repositories` vastaa tiedon tallennuksesta tietokantaan sekä csv-tiedostoihin, `services` vastaa sovelluslogiikasta ja `ui` käyttöliittymästä. Hakemisto `entities` sisältää luokkia ohjelman muuttujille.
## Tietojen tallennus
Hakemiston `repositories` luokat vastaavat tietojen tallentamisesta. Luokka`UserRepository` tallentaa käyttäjätunnuksiin liittyvän datan SQLite-tietokantaan. Tietokannassa on taulu `users`, johon tunnus tallennetaan käyttäjätunnus|salasana pareina. Luokka `CsvRepository` vastaa csv-tiedostojen perustoiminnallisuuksiasta, kuten tiedoston luomisesta ja tyhjentämisestä. Luokat `NoteRepository` ja `CourseRepository` tallentavat tiedon kurssisuorituksista ja muistiinpanoista omiin csv-tiedostoihinsa hyödyntäen `CsvRepository`-luokkaa 
## Sovelluslogiikka
Sovelluslogiikasta vastaa luokka `TrackerService`. 
Luokan metodeja ovat esimerkiksi seuraavat:
- `login(username, password)`, `logout`
- `create_user`, `create_note`, `create_course`
- `get_users`, `get_notes`, `get_courses`
- `delete_note`, `delete_course`

## Toiminnallisuudet
### Kirjautuminen
Kirjautumisnäkymän kenttiin syötetään käyttäjätunnus ja salasana, jonka jälkeen "Kirjaudu"-painike käynniostää tapahtumankäsittelijän.

![Kirjautuminen](https://user-images.githubusercontent.com/80783887/115996379-a3db0380-a5e7-11eb-829f-104a34221397.png)

Sovelluslogiikan "login" vaihe kutsuu käyttäjärepositiota, joka tarkastaa käyttäjätietokannasta, ovatko tunnus ja salasana oikein. 
