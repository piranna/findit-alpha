from google.appengine.ext import db
from google.appengine.ext.db import polymodel


# Icon
class Icon(db.Model):
#	image = "http://www.google.com/mapfiles/turkey.png";
#	shadow = "http://www.google.com/mapfiles/turkeyshadow.png";
#	iconSize = new GSize(59, 62);
#	shadowSize = new GSize(91, 62);
#	iconAnchor = new GPoint(37, 59);
#	infoWindowAnchor = new GPoint(31, 8);

	image = db.StringProperty()
	shadow = db.StringProperty()
#	iconSize = GSize(59, 62);
#	shadowSize = GSize(91, 62);
	iconAnchor = db.GeoPtProperty();
	infoWindowAnchor = db.GeoPtProperty();


# Metadata
class Metadata(polymodel.PolyModel):
	name = db.StringProperty()
	description = db.StringProperty(multiline=True)
	icon = Icon()

	autor = db.UserProperty(auto_current_user_add=True)
	date = db.DateTimeProperty(auto_now_add=True)

#	visibility = db.ListProperty(users.User, default=None)				# Visible for all
#	edit = db.ListProperty(users.User, default=[users.current_user])	# Editable only for author
#	admin = db.ListProperty(users.User, default=[users.current_user])	# Administable only for author

	def to_xml_internal(self):
		xml = "<name>"+self.name+"</name>"
		if self.description:
			xml += "<description>"+self.description+"</description>"
		return xml


# Marker
class Marker(Metadata):
	position = db.GeoPtProperty()

	#collection = db.ReferenceProperty(Collection,
	#									collection_name="markers")

	def to_xml(self):
		return "<marker>" + self.to_xml_internal() + "</marker>"

	def to_xml_internal(self):
		xml = Metadata.to_xml_internal(self)
		pos = str(self.position).split(",")
		return xml + "<position lat='"+pos[0]+"' lon='"+pos[1]+"'/>"


# Collection
class Collection(Metadata):
	markers = []
#	markers = db.ListProperty(Marker, default=None)

	#collection_folder = db.ReferenceProperty(Collection_Folder,
	#											collection_name="subfolders")

	def to_xml(self):
		return "<collection>" + self.to_xml_internal() + "</collection>"

	def to_xml_internal(self):
		xml = Metadata.to_xml_internal(self)
		for marker in self.markers:
			xml += marker.to_xml()
		return xml


class Collection_Folder(Collection):
	subfolders = []
#	subfolders = db.ListProperty(Collection, default=None)

	def to_xml(self):
		return "<collection_folder>" + self.to_xml_internal() + "</collection_folder>"

	def to_xml_internal(self):
		xml = Collection.to_xml_internal(self)
		for subfolder in self.subfolders:
			xml += subfolder.to_xml()
		return xml


#class Collection_External(Collection):
#	url = db.StringProperty()


# User
class User(db.Model):
	id = db.UserProperty(auto_current_user_add=True)
	folders = []
#	folders = db.ListProperty(Collection, default=None)
