from google.appengine.ext import webapp

import os
from google.appengine.api import users
from google.appengine.ext.webapp import template

from . import HTML_PATH


class MainPage(webapp.RequestHandler):

	def get(self):
		user = users.get_current_user()

		if user:
			template_values = {
								'nickname': user.nickname(),
								'logout_url': users.create_logout_url("/"),
								'is_current_user_admin': users.is_current_user_admin(),
								}

			path = os.path.basename(os.path.splitext(__file__)[0])+'.html'
			path = os.path.join(HTML_PATH, path)
			self.response.out.write(template.render(path, template_values))

		else:
			self.redirect(users.create_login_url(self.request.uri))
