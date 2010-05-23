from google.appengine.ext import db
from google.appengine.ext.db import polymodel


# Alert_Icon
class Alert_Icon(db.Model):
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


# Alert_Collection
class Alert_Collection(polymodel.PolyModel):
	name = db.StringProperty()
	icon = Alert_Icon()

	collection = db.SelfReferenceProperty(collection_name="subfolders")

#	visibility = db.ListProperty(db.UserProperty())
#	edit = db.ListProperty(db.UserProperty())
#	admin = db.ListProperty(db.UserProperty())

class Alert_Collection_External(Alert_Collection):
	url = db.StringProperty()

class Alert_Collection_Folder(Alert_Collection):
#	alerts = db.ListProperty(Alert)
#	subfolders = db.ListProperty(Alert_Collection)
	pass


# Alert
class Alert(db.Model):
	icon = Alert_Icon()
	autor = db.UserProperty()
	description = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
	position = db.GeoPtProperty()

	collection = db.ReferenceProperty(Alert_Collection_Folder,
										collection_name="alerts")
