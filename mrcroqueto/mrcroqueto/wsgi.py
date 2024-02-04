"""
WSGI config for mrcroqueto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mrcroqueto.settings.production")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mrcroqueto.settings.local")

# application = get_wsgi_application()

from dj_static import Cling

"""from whitenoise import WhiteNoise

application = WhiteNoise(get_wsgi_application(), root=settings.STATIC_ROOT)"""

application = Cling(get_wsgi_application())
