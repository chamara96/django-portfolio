import os
import sys
from MyPortfolio.wsgi import application

sys.path.insert(0, os.path.dirname(__file__))

environ = os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyPortfolio.settings")