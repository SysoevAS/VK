import os
from django.core.wsgi import get_wsgi_application

try:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'service_vk.settings'
    application = get_wsgi_application()
except Exception as e:
    print('Failed to load application: %s' % e)
