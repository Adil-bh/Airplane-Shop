"""
ASGI config for airplane_shop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "airplane_shop.settings")

from django.conf import settings

print(settings.USE_I18N)

application = get_asgi_application()
