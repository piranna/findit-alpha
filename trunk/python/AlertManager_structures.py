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


# AlertCollection
class AlertCollection(polymodel.PolyModel):
	title = db.StringProperty()
	description = db.StringProperty(multiline=True)
	icon = Alert_Icon()

	collection = db.SelfReferenceProperty(collection_name="subfolders")

#	visibility = db.ListProperty(db.UserProperty())
#	edit = db.ListProperty(db.UserProperty())
#	admin = db.ListProperty(db.UserProperty())

class AlertCollection_External(AlertCollection):
	url = db.StringProperty()

class AlertCollection_Folder(AlertCollection):
#	alerts = db.ListProperty(Alert)
#	subfolders = db.ListProperty(AlertCollection)
	pass


# Alert
class Alert(db.Model):
	title = db.StringProperty()
	description = db.StringProperty(multiline=True)
	icon = Alert_Icon()

	#autor = db.UserProperty()

	date = db.DateTimeProperty(auto_now_add=True)
	position = db.GeoPtProperty()

	collection = db.ReferenceProperty(AlertCollection_Folder,
										collection_name="alerts")
