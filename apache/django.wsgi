import os
import sys
import site

sys.path.append('/mnt/sites/opiticiwan.ca/')
site.addsitedir('/mnt/sites/opiticiwan.ca/python-env/lib/python2.7/site-packages') 

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
