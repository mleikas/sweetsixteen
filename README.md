# sweetsixteen

## Backlog

[Linkki backlogeihin](https://docs.google.com/spreadsheets/d/1WaXkt1bA5ho_e-IfcfUK9stK1fLb32ynSzqMo0fLLdM/edit?usp=sharing)

## Asennus

Tietokannan alustus onnistuu ajamalla sovelluksen juurihakemistossa komento:

`poetry run invoke build`

## Testaus

Testit saadaan tehtyä komennolla

```bash
poetry run invoke test
```

## Testikattavuusraportti

Testikattavuusraportin saa htmlcov kansioon komenolla:

```bash
poetry run invoke coverage-report
```

## Pylint

Tiedoston [.pylintrc](./.pylintrc) tarkastukset tehdään komennolla:

```bash
poetry run invoke lint
```
