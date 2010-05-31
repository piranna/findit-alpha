from google.appengine.ext import webapp

from google.appengine.api import users
from google.appengine.ext import db

from db_structures import *


class MarkersManager(webapp.RequestHandler):

	def post(self):
		command = self.request.get('command')

		if command == "Add_Marker":
			self.Add_Marker()
		
		elif command == "Add_Collection":
			command_type = self.request.get('type')

#			if command_type == "External":
#				self.Add_Collection_External()

			if command_type == "Folder":
#			elif command_type == "folder":
				self.Add_Collection_Folder()
				

	def get(self):
		User.get_or_insert(str(users.get_current_user())).folders.append(Collection.gql("WHERE name = :name", name="Gasolineras").get())
		for folder in User.get_or_insert(str(users.get_current_user())).folders:
			self.response.out.write(folder.to_xml())



#		self.response.out.write("<markers>")

#		for marker in Marker.all():
#			self.response.out.write('<marker>')

#			self.response.out.write(	'<name lat="'+position[0]+'" lng="'+position[1]+'"/>')
#			self.response.out.write(	'<description lat="'+position[0]+'" lng="'+position[1]+'"/>')
#			self.response.out.write(	'<icon>')

#			self.response.out.write(		'<image url="'+marker.icon.image+'"/>')
#			self.response.out.write(		'<shadow url="'+marker.icon.shadow+'"/>')
#			self.response.out.write(		'<iconAnchor />')
#			self.response.out.write(		'<infoWindowAnchor />')

#			self.response.out.write(	'</icon>')

#			position = str(marker.position).split(",")
#			self.response.out.write(	'<position lat="'+position[0]+'" lng="'+position[1]+'"/>')

#			self.response.out.write('</marker>')

#		self.response.out.write("</markers>")


	def Add_Marker(self):
		# Create new alert
		alert = Marker(	name = self.request.get('name'),
						description = self.request.get('description'),
						position = db.GeoPt(self.request.get('lat'),
											self.request.get('lng')))

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


	def Add_Collection_Folder(self):
		# Create new alert
		collection = Collection_Folder(self.request.get('title'),
										self.request.get('description'))

		# Set collection icon
		#self.request.get('icon')

		# Store collection
		collection.put()


#	def Add_Collection_External(self):
#		# Create new alert
#		collection = AlertCollection_External(	self.request.get('title'),
#												self.request.get('description'))

#		# Set collection icon
#		#self.request.get('icon')


#		# Store collection
#		collection.put()
