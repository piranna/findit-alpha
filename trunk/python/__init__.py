from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


import os
HTML_PATH = os.path.join(os.path.dirname(__file__), '..', 'html')

import MainPage
import AlertManager


# Launch app
run_wsgi_app(webapp.WSGIApplication([('/', MainPage.MainPage)
									,('/alertManager', AlertManager.AlertManager)],
									debug=True))