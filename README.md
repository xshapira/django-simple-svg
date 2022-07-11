# django-simple-svg

[![PyPI version](https://badge.fury.io/py/django-simple-svg.svg)](https://badge.fury.io/py/django-simple-svg)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/django-simple-svg.svg)](https://pypi.python.org/pypi/django-simple-svg/)
[![PyPI Supported Django Versions](https://img.shields.io/pypi/djversions/django-simple-svg.svg)](https://docs.djangoproject.com/en/dev/releases/)
[![GitHub Actions (Code quality and tests)](https://github.com/mixxorz/slippers/workflows/Code%20quality%20and%20tests/badge.svg)](https://github.com/xshapira/django-simple-svg)

A simple plugin that adds an ``svg`` template tag to inline your SVGs in your
Django templates.

### This is an updated version of this repo

[https://github.com/mixxorz/django-inline-svg]()

Huge credit goes to [Mitchel Cabuloy](https://github.com/mixxorz)

## Installation

Install it from pypi.

```bash
pip install django-simple-svg
```

Add ```simple_svg``` to your ```INSTALLED_APPS```.

```python
    INSTALLED_APPS = (
        ...
        'simple_svg',
        ...
    )
```

## Usage

Store your SVGs in folder named ```svg``` at the root of any of your static file
directories.

```bash
    my_app
    |-- static
    |   |-- svg
    |       |-- logo.svg
    |       |-- check.svg
    |       |-- cross.svg
```

Use the ```svg``` template tag.

```django
    {% load svg %}

    <h1 class="logo">{% svg 'logo' class="css-class" height="16" width="16" %}</h1>
```

You can set ```SVG_DIRS``` to control where to look for your svgs.

```python
    # settings.py

    SVG_DIRS=[
        os.path.join(BASE_DIR, 'my-svgs')
    ]
```

## Support

The tests are run against Django 1.8 to 4.0.6 on Python 2.7, 3.4, 3.5, 3.6, 3.8, 3.10.

## License

MIT
