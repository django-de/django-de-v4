#  The website of the German Django Association - v4.0

### Installation for local development

Software Requirements:

- Python 2.7 or 3.x
- PostgreSQL
- node

Copy the sample settings file and adjust the settings according to your needs:

    $ cp djde/settings/local.py.example djde/settings/local.py

Install the requirements and create a blank database, migrate all the tables:

    $ mkvirtualenv djde
    $ pip install -r requirements.txt
    $ manage.py migrate

Create a superuser on first install:

    $ manage.py createsuperuser

The static file compilation is done with Node dependencies. On a Mac install
node via Homebrew:

    $ brew install node

To compile all static files simply run:

    $ make all

Finally collect those static files and start the development server:

    $ manage.py collectstatic
    $ manage.py runserver

#### Static files during development

You can watch for changes of CSS and JS files and have them re-compiled
on-the-fly. Run each command in a separate shell.

    $ make js watch=1
    $ make css watch=1

#### How static files are treated

* All client/browser related files are stored in `client/`.
* Static files which don't need processing are in `client/assets`.
* CSS and JS  are compiled into the `build/` folder using a `make` command.
* Django's `collectstatic` takes everything from the `build/` folder plus
  the "classic" application static files and puts them in `<venv>/var/static/`.
  This is also the folder we serve with the webserver.

For CSS we use a factory of: Node-Sass for CSS compilation + autoprefixer.

For JS we use browserify to collect all dependencies, from `client/js` as well
as from the `node_modules` into one file. We transform that with Babel from ES6
to ES5 for compatibility reasons. We compress that with uglify.

### The Theme

We're using a theme called [Jango][jango] for the overall appearance. This name
is totally a coincidence and it's not related to the Django Python Framework.

However this theme is not free, and not open source. We ship this code with a
massively stripped down variant, which is not usable if you want to extend the
site. The German Django Association owns a license of this theme, and if you
want to extend our site, you can ask to get the full package.

If you intend to e.g. fork this package you either have to obtain the theme
or just drop the entire styles and recreate them.

[jango]: http://themehats.com/themes/jango/

### Heroku Setup

Heroku has a separate settings module in `djde.settings.heroku`. We serve
static files directly from Heroku using Cling, but media uploads are stored
in a S3 bucket.

Initial Configuration:

```
heroku buildpacks:set https://github.com/heroku/heroku-buildpack-python
heroku buildpacks:add --index=1 https://github.com/heroku/heroku-buildpack-nodejs

heroku config:add DJANGO_SETTINGS_MODULE=djde.settings.heroku
heroku config:add DJANGO_SECRET_KEY=secret
heroku config:add DJANGO_ADMIN_EMAIL=root@localhost

heroku config:add AWS_ACCESS_KEY_ID=key
heroku config:add AWS_SECRET_ACCESS_KEY=secret
heroku config:add AWS_STORAGE_BUCKET_NAME=bucket

# You likely won't need to setup this manually, it's set once you
# select a Heroku PostgreSQL db.
heroku config.add DATABASE_URL=postgres://user:pass@localhost:5432/dbname
```

To deploy simply push your branch to Heroku. If necessary, migrate the
database.

```
git push heroku master
heroku run python manage.py migrate
```
