django-de-website
=================

Installation
------------

.. code-block:: bash

    $ # Clone repository
    $ git clone git@github.com:django-de/django-de-website.git

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
