# **OT-Harjoitustyö**
## Opintoseuraaja
Sovelluksen avulla käyttäjällä on mahdollista pitää kirjaa omista opinto suorituksistaan sekä opintomenestyksestä. 

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Vaatimusmäärittely.md)

[Työaikakirjanpito](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Työaikakirjanpito.md)

[Arkkitehtuuri](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Arkkitehtuuri.md)

## Asennus

Asenna riippuvuudet komennolla:
'''
poetry install
'''
Alusta sovellus komennolla:
poetry run invoke build

Käynnistä sovellus komennolla:
poetry run invoke start

## Komentorivi

Testaukset voi suorittaa komennolla:
poetry run invoke test

Testikattavuuden voi tarkistaa komennolla:
poetry run invoke coverage

Testikattavuusraportin saa komennolla:
poetry run invoke coverage_raport


