# project0-python-django-api

## Backend

### Branches testables
- Crypto: Tiene la cotizacion de dolar y cryptos.
- dj-rest-auth: Login/Registro

### Como iniciar server y bot
- `cd backend`
- `pipenv shell`

- En terminales distintas:
    - `celery -A config  worker -l info` (bot)
    - `py .\manage.py runserver` (server)

### Endpoints
    Cuando entran al server http://127.0.0.1:8000/ les aparece la lista.