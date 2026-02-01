"""
WSGI config for MdRiyadulIslamRatul_REG_ICT_WADP_L4_001145_JobPortal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MdRiyadulIslamRatul_REG_ICT_WADP_L4_001145_JobPortal.settings')

application = get_wsgi_application()
