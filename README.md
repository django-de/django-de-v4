# django-de 4.0

# Heroku setup

heroku buildpacks:set https://github.com/heroku/heroku-buildpack-python
heroku buildpacks:add --index=1 https://github.com/heroku/heroku-buildpack-nodejs

heroku config:add DJANGO_SETTINGS_MODULE=djde.settings.heroku
heroku config:add DJANGO_SECRET_KEY=secret
heroku config:add DJANGO_ADMIN_EMAIL=root@localhost

# Done once you setup the Heroku Postgres db
# heroku config.add DATABASE_URL=postgres://user:pass@localhost:5432/dbname

git push heroku master
heroku run python manage.py migrate
