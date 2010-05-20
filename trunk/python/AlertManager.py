from google.appengine.ext import webapp

from google.appengine.api import users
from google.appengine.ext import db


class AlertCollection(db.Model):
	name = db.StringProperty()
#	icon

#	visibility = db.ListProperty(db.UserProperty())
#	edit = db.ListProperty(db.UserProperty())
#	admin = db.ListProperty(db.UserProperty())


class Alert(db.Model):
	autor = db.UserProperty()
	description = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
	position = db.GeoPtProperty()

	collection = db.ReferenceProperty(AlertCollection, collection_name='alerts')


# AlertManager
class AlertManager(webapp.RequestHandler):

	def post(self):
		alert = Alert(autor			= users.get_current_user(),
						description	= self.request.get('description'),
						position	= db.GeoPt(self.request.get('latitud'), self.request.get('longitud')))

		collection = self.request.get('collection')
		alerts = AlertCollection.all().get()
		if(alerts
		and collection in alerts.name):
			collection = AlertCollection.gql("WHERE name = :1", collection).get()
		else:
			collection = AlertCollection(name=collection).put()
		alert.collection = collection

		alert.put()


	def get(self):
		alerts = db.GqlQuery("SELECT * FROM Alert")

		self.response.out.write("<markers>\n")

		for alert in alerts:
			position = str(alert.position).split(",")

			self.response.out.write('<marker')
			self.response.out.write(' latitud="' + position[0] + '"')
			self.response.out.write(' longitud="' + position[1] + '"')
			if alert.collection:
				self.response.out.write(' collection="' + alert.collection.name + '"')
			self.response.out.write('/>')

		self.response.out.write("</markers>\n")
