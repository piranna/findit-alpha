from google.appengine.ext import webapp

from google.appengine.api import users
from google.appengine.ext import db

from AlertManager_structures import *


class AlertManager(webapp.RequestHandler):

	def post(self):
		# Create new alert
		alert = Alert(autor			= users.get_current_user(),
						description	= self.request.get('description'),
						position	= db.GeoPt(self.request.get('latitud'), self.request.get('longitud')))

		# Set alert collection
		collection = self.request.get('collection')
		alerts = Alert_Collection_Folder.all().get()
		if(alerts
		and collection in alerts.name):
			collection = Alert_Collection_Folder.gql("WHERE name = :1", collection).get()
		else:
			collection = Alert_Collection_Folder(name=collection).put()
		alert.collection = collection

		# Store alert
		alert.put()


	def get(self):
		self.response.out.write("<markers>\n")

		for alert in Alert.all():
			position = str(alert.position).split(",")

			self.response.out.write('<marker')
			self.response.out.write(' latitud="' + position[0] + '"')
			self.response.out.write(' longitud="' + position[1] + '"')
			if alert.collection:
				self.response.out.write(' collection="' + alert.collection.name + '"')
			self.response.out.write('/>')

		self.response.out.write("</markers>\n")
