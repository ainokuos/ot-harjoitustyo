# Testausdokumentti

Ohjelmaa on testattu unittestilla. testaus on suoritettu yksikkö- ja integraatiotasolla. Käyttöjärjestelmä on testattu manuaalisesti.

## Yksikkö- ja integraatiotestaus

### Repositorio-luokat
Luokista `NoteRepository`, `CourseRepository` ja `UserRepository` testataan tiedon tallennus, luku ja poisto. Testaukseen kuuluu myös yhteyden luominen tiedostoon sekä luokkien `NoteRepository` ja `CourseRepository` perustoiminnallisuudet yhdistävän `CsvRepositoryn`-luokan testaaminen. 

### Sovelluslogiikka
Luokasta `TrackerService` testataan käyttääjn luominen ja riippuvuus `UserRepository`-luokan välillä. Kirjautumiseen käytettävä "login"-metodi testataan.

### Testikattavuusraportti
Sovelluksen testauksen haarautumakattavuus on 81%.
![Testikattavuus](https://user-images.githubusercontent.com/80783887/118104193-7cf04000-b3e3-11eb-89d4-c9d65ea23fe1.png)
Testaamattajäävät sovelluslogiikan riippuvuudet `NoteRepository` ja `CourseRepository` luokkien välillä.

### Järjestelmätestaus
Käyttöliittymä on testattu manuaalisesti. Sovelluksen toiminta on testattu loogisilla virhetilanteilla, jotka nostavat virheilmoituksen käyttäjälle. 



