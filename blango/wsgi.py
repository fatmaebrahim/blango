"""
WSGI config for blango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

#wsgi.py is used by an application server to load your web server in production,


import os
#before using config
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blango.settings')

# application = get_wsgi_application()

#after
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blango.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()