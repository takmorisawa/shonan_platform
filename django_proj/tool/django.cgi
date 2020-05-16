#!/home/xs324884/.linuxbrew/Cellar/python/3.7.7_1/bin/python3.7
import sys, os
 
#sys.path.insert(0, "~/.linuxbrew/bin/python3")
# sys.path.append("/home/xs324884/.linuxbrew/Cellar/python/3.7.7_1/lib/python3.7/site-packages")
sys.path.append("/home/xs324884/xs324884.xsrv.jp/public_html/shonan_platform/django_proj") 

os.environ['DJANGO_SETTINGS_MODULE'] = "django_proj.settings"
 
from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)


