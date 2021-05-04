# Arkkitehtuurikuvaus
## Rakenne
Rakenne noudattaa kerrosarkkitehtuuria
![Arkkitehtuuri](https://user-images.githubusercontent.com/80783887/117005417-e8555600-acef-11eb-8dc1-76fc6185da9a.png)

Hakemisto `repositories` vastaa tiedon tallennuksesta tietokantaan sekä csv-tiedostoihin, `services` vastaa sovelluslogiikasta ja `ui` käyttöliittymästä. Hakemisto `entities` sisältää luokkia ohjelman muuttujille.
## Toiminnallisuudet
# Kirjautuminen
Kirjautumisnäkymän kenttiin syötetään käyttäjätunnus ja salasana, jonka jälkeen "Kirjaudu"-painike käynniostää tapahtumankäsittelijän.

![Kirjautuminen](https://user-images.githubusercontent.com/80783887/115996379-a3db0380-a5e7-11eb-829f-104a34221397.png)

Sovelluslogiikan "login" vaihe kutsuu käyttäjärepositiota, joka tarkastaa käyttäjätietokannasta, ovatko tunnus ja salasana oikein. 
