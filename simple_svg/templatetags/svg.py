from __future__ import absolute_import
import logging
import os

from django import template
from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.exceptions import ImproperlyConfigured
from django.utils.safestring import mark_safe

from simple_svg.exceptions import SVGNotFound

logger = logging.getLogger(__name__)
register = template.Library()


@register.simple_tag
def svg(filename, *args, **kwargs):
    SVG_DIRS = getattr(settings, "SVG_DIRS", [])

    if type(SVG_DIRS) != list:
        raise ImproperlyConfigured("SVG_DIRS setting must be a list")

    path = None

    if SVG_DIRS:
        for directory in SVG_DIRS:
            svg_path = os.path.join(
                directory, "{filename}.svg".format(filename=filename)
            )

            if os.path.isfile(svg_path):
                path = svg_path
    else:
        path = finders.find(
            os.path.join("svg", "{filename}.svg".format(filename=filename)), all=True
        )

    if not path:
        message = "SVG '{filename}.svg' not found".format(filename=filename)

        if settings.DEBUG:
            raise SVGNotFound(message)
        logger.warning(message)
        return ""

    # Sometimes path can be a list/tuple if there's more than one file found
    if isinstance(path, (list, tuple)):
        path = path[0]

    with open(path) as svg_file:
        svg = svg_file.read()

    if kwargs:
        attributes = " ".join([f'{k}="{v}"' for k, v in kwargs.items()])
        svg = svg.replace("<svg", f"<svg {attributes}")

    svg = mark_safe(svg)

    return svg
