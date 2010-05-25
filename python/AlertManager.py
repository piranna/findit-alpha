from google.appengine.ext import webapp

from google.appengine.api import users
from google.appengine.ext import db

from AlertManager_structures import *


class AlertManager(webapp.RequestHandler):

	def post(self):
		command = self.request.get('command')

		if command == "Alert_Add":
			self.Add_Alert()
		
		elif command == "AlertCollection_Add":
			command_type = self.request.get('type')

			if command_type == "external":
				self.Add_AlertCollection_External()

			elif command_type == "folder":
				self.Add_AlertCollection_Folder()
				

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


	def Add_Alert(self):
		# Create new alert
		alert = Alert(	self.request.get('title'),
						self.request.get('description'),
						#autor = users.get_current_user(),
						db.GeoPt(self.request.get('latitud'),
								self.request.get('longitud')))

		# Set alert icon
		#self.request.get('icon')

		# Set alert collection
		collection = self.request.get('collection')
		alerts = AlertCollection_Folder.all().get()
		if(alerts
		and collection in alerts.name):
			collection = AlertCollection_Folder.gql("WHERE name = :1", collection).get()
		else:
			collection = AlertCollection_Folder(name=collection).put()
		alert.collection = collection

		# Store alert
		alert.put()


	def Add_AlertCollection_External(self):
		# Create new alert
		collection = AlertCollection_External(	self.request.get('title'),
												self.request.get('description'))

		# Set collection icon
		#self.request.get('icon')


		# Store collection
		collection.put()


	def Add_AlertCollection_Folder(self):
		# Create new alert
		collection = AlertCollection_Folder(self.request.get('title'),
											self.request.get('description'))

		# Set collection icon
		#self.request.get('icon')

		# Store collection
		collection.put()
