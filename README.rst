django-de-website
=================

Installation
------------

.. code-block:: bash

    $ # Clone repository
    $ git clone git@github.com:django-de/django-de-website.git

    $ npm install
    $ pipenv install

    $ # run tests
    $ pipenv run py.test


Development settings
--------------------

Create the file `djangode/settings.py` with the following content, feel free
to add some custom settings for local development:

.. code-block:: python

    from djangode.conf.dev_settings import *


Setup the database for development
----------------------------------

For Development:

.. code-block:: bash

    $ createdb djangode_dev

After all you can migrate the database:

.. code-block:: bash

    $ pipenv run ./manage.py migrate


Static file compilation
-----------------------

How static files are treated

- All client/browser related files are stored in client/.
- Static files which don't need processing are in client/assets.
- CSS and JS are compiled into the build/ folder using a make command.
- Asset files are simply copied to the build/ folder.
- Django's collectstatic takes everything from the build/ folder plus the
  "classic" application static files and puts them in `STATIC_ROOT`.
  This is also the folder we serve with the webserver.

For CSS we use a factory of: Node-Sass for CSS compilation + autoprefixer.

For JS we use browserify to collect all dependencies, from client/js as well as
from the node_modules into one file. We transform that with Babel from ES6 to
ES5 for compatibility reasons. We compress that with uglify.

.. code-block:: bash

    $ npm install

Staring the server & superuser
------------------------------

.. code-block:: bash

    $ # Create a new super user
    $ pipenv run ./manage.py createsuperuser

Now you can run the webserver and start using the site.

.. code-block:: bash

   $ pipenv run ./manage.py runserver

This starts a local webserver on `localhost:8000 <http://localhost:8000/>`_. To
view the administration interface visit `/admin/ <http://localhost:8000/admin/>`_


Resources
---------

* `Documentation <https://github.com/django-de/django-de-website>`_
* `Bug Tracker <https://github.com/django-de/django-de-website/issues>`_
* `Code <https://github.com/django-de/django-de-website>`_
