# project0-python-django-api

## Backend

### Project explanaition
Testing of Django Rest Framework, deployed using Docker-Heroku-PostgreSQL.


### Functional branches
- Signals: Deployed on heroku. Custom user with dj-rest-auth library and JWT and notification to email when Model is updated.
    - Endpoints:
        - https://young-citadel-29924.herokuapp.com/accounts/register/
        - https://young-citadel-29924.herokuapp.com/accounts/login/
- Crypto: Not deployed. Models with crpto data and celery bot scraper filling each Model.


### To be added
- Elastic Search instead of Django-ORM
- Channels