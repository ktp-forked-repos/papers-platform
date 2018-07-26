import os
import sys

path = os.path.expanduser('~/papers_platform')
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'papers_platform.settings.dev'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "papers_platform.settings.dev")
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
