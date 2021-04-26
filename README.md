# **OT-Harjoitustyö**
## Opintoseuraaja
Sovelluksen avulla käyttäjällä on mahdollista pitää kirjaa omista opinto suorituksistaan sekä opintomenestyksestä. 
### Viimeisin versio
[Opintoseuraaja](https://github.com/ainokuos/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Vaatimusmäärittely.md)

[Työaikakirjanpito](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Työaikakirjanpito.md)

[Arkkitehtuuri](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:
```
poetry install
```

2. Alusta sovellus komennolla:
```
poetry run invoke build
```

3.Käynnistä sovellus komennolla:
```
poetry run invoke start
```
## Komentorivi

Testaukset voi suorittaa komennolla:
```
poetry run invoke test
```
Testikattavuuden voi tarkistaa komennolla:
```
poetry run invoke coverage
```
Testikattavuusraportin saa komennolla:
```
poetry run invoke coverage-report
```
Laatutarkistuksen voi suorittaa komennolla:
```
poetry run invoke lint
```
