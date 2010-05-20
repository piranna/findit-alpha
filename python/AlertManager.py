from google.appengine.ext import webapp

from google.appengine.api import users
from google.appengine.ext import db


class Alert(db.Model):
	autor = db.UserProperty()
	desc = db.StringProperty(multiline=True)
	fecha = db.DateTimeProperty(auto_now_add=True)
	pos = db.GeoPtProperty()


class AlertManager(webapp.RequestHandler):

	def post(self):
		alert = Alert()

		if users.get_current_user():
			alert.autor = users.get_current_user()

		alert.desc = self.request.get('descripcion');
		alert.pos = db.GeoPt(self.request.get('latitud'), self.request.get('longitud'))
		alert.put()


	def get(self):
		alerts = db.GqlQuery("SELECT * FROM Alert")

		self.response.out.write("<markers>\n")

		for alert in alerts:
			alert = str(alert.pos).split(",")

			self.response.out.write('<marker')
			self.response.out.write(' lat="' + alert[0] + '"')
			self.response.out.write(' lon="' + alert[1] + '"')
			self.response.out.write('/>')

		self.response.out.write("</markers>\n")
