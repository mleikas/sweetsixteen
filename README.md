# sweetsixteen

![Workflow badge](https://github.com/mleikas/sweetsixteen/workflows/CI/badge.svg)

[![codecov](https://codecov.io/gh/mleikas/sweetsixteen/branch/main/graph/badge.svg?token=ywnp6wfOY9)](https://codecov.io/gh/mleikas/sweetsixteen)

## Backlog

[Linkki backlogeihin](https://docs.google.com/spreadsheets/d/1WaXkt1bA5ho_e-IfcfUK9stK1fLb32ynSzqMo0fLLdM/edit?usp=sharing)

[Linkki viimeisimpään releaseen](https://github.com/mleikas/sweetsixteen/releases/tag/sprint2_release)

## Asennus

Poetry tulee olla asennettuna ohjelman suoritusta varten. Tarvittavien kirjastojen asennus onnnistuu komennolla

```bash
poetry install
```

Tietokannan alustus onnistuu ajamalla sovelluksen juurihakemistossa komento:

```bash
poetry run invoke build
```

## Suoritus

Ohjelma suoritetaan komennolla

```bash
poetry run invoke start
```

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

## Definition of Done

- Acceptance criteria for a user story are met
- Unit/integration tests created with at least 85% branch coverage
- Code pushed to GitHub			
- Code accepted by tests in Github Actions
