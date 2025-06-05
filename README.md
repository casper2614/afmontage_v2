# Afmontage Tracking – Broshuis B.V.

## Installatie

Zorg dat je Python en pip geïnstalleerd hebt. Volg daarna deze stappen om het project op te starten:

1. Installeer de benodigde dependencies:
```bash
pip install -r requirements.txt
```

2. Maak en voer de database migraties uit:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Maak een superuser-account aan om toegang te krijgen tot de admininterface:
```bash
python manage.py createsuperuser
```

4. Start de ontwikkelserver:
```bash
python manage.py runserver 8000
```

De website is nu bereikbaar op: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Licentie

Deze software is gelicenseerd onder de **GNU General Public License v3.0 (GPLv3)**. De volledige licentie vind je in het bestand [`LICENSE.md`](./LICENSE.md).

## Auteurs

- **Casper Janssen** [@casper2614](https://www.github.com/casper2614)  
- **Wessel Janssen**
