import re
import os
import datetime

from python.FindIt.db_structures import *
from python.FindIt.db_structures import Oil


tmp_path = "tmp"


exp = "<tr><td>(.+?)</td><td>(.+?)\s*</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td></tr>"

	# 0 Provincia
	# 1 Localidad
	# 2 Direccion
	# 3 Toma de datos (fecha)
	# 4 Precio
	# 5 Rotulo (nombre)
	# 6 Tipo Venta
	# 7 Rem.
	# 8 Horario


folder = Collection_Folder.get_or_insert("Gasolineras", name="Gasolineras"
														#,icon=Icon()
														)

for filename in Oil.filenames:

	subfolder = Collection_Folder.get_or_insert(filename, name=filename
														#,icon=Icon()
														)
	folder.subfolders.append(subfolder)

	f = file(os.path.join(tmp_path,filename+".xls")).read()
	f = re.sub('>\s+<','><', f)

	lines = re.findall(exp, f)
	for line in lines:

		station = Oil.Oil_Station.get_or_insert(line[5], name = line[5]
												,scheudle = line[8]
												,address = (line[2]+"\n"+line[1]+" ("+line[0]+")").decode("latin1")
												)

		date = line[3].split('/')

		oil_take = Oil.Oil_Take(type = filename
								,date = datetime.date(int(date[2]),int(date[1]),int(date[0]))
								,price = float(line[4].replace(',','.'))
								,oil_station = station
								).put()

		subfolder.markers.append(station)
