from google.appengine.ext import db

from . import Marker


filenames = ('biodiesel_prueba',
			'gasoleoA_prueba')

#filenames = ('biodiesel',
#			'gasoleoA',
#			'gasoleoAplus',
#			'gasolina95',
#			'gasolina98')


class Oil_Station(Marker):
	scheudle = db.StringProperty()
	address = db.PostalAddressProperty()
	# Tipo de venta
	# Rem


class Oil_Take(db.Model):
	type = db.StringProperty(choices=filenames)
	date = db.DateProperty()
	price = db.FloatProperty()

	oil_station = db.ReferenceProperty(Oil_Station,
										collection_name='oil_takes')
