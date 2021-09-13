django-svg
==================================

A simple plugin that adds an ``svg`` template tag to inline your SVGs in your
Django templates.

This an updated version of this repo: <br />
[https://github.com/mixxorz/django-inline-svg]()

All credits goes to [Mitchel Cabuloy](https://github.com/mixxorz)


Installation
------------

Install it from pypi.


    $ pip install django-svg

Add ``svg`` to your ``INSTALLED_APPS``.


    INSTALLED_APPS = (
        ...
        'django_svg',
        ...
    )

Usage
-----

Store your SVGs in folder named ``svg`` at the root of any of your static file
directories.

    my_app
    |-- static
    |   |-- svg
    |       |-- logo.svg
    |       |-- check.svg
    |       |-- cross.svg

Use the ``svg`` template tag.

    {% load svg %}

    <h1 class="logo">{% svg 'logo' class="css-class" height="16" width="16" %}</h1>

You can set ``SVG_DIRS`` to control where to look for your svgs.

    # settings.py

    SVG_DIRS=[
        os.path.join(BASE_DIR, 'my-svgs')
    ]

Support
-------

The tests are run against Django 1.8 to 3.2 on Python 2.7, 3.4, 3.5, 3.6, 3.8.

License
-------

MIT
