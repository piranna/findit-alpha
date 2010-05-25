function Alert_Add(title,description, latitud,longitud, collection)
{
	GDownloadUrl("alertManager", map.clearOverlays,
				"command=" + "Alert_Add"
				+"title=" + title
				+"description=" + description
				+ "&icon=" + icon
				+ "&latitud=" + latitud
				+ "&longitud=" + longitud
				+ "&collection=" + collection);
}

function AlertCollection_Add(type, title,description, icon=null)
{
	GDownloadUrl("alertManager", null,
				"command=" + "AlertCollection_Add"
				+"tipe=" + type
				+"title=" + title
				+"description=" + description
				+ "&icon=" + icon);
}

function Load_Alerts()
{
	GDownloadUrl("alertManager",
				function(data, responseCode)
				{
					// Get alerts
					var xml = GXml.parse(data);
					var markers = xml.documentElement.getElementsByTagName("marker");

					// for every alert,
					// get it's coordinates and put mark in the map
					for(var i = 0; i < markers.length; i++)
					{
						// Get x and y coordinates
						var x = markers[i].getAttribute("latitud");
						var y = markers[i].getAttribute("longitud");

						// If we have get x and y coordinates,
						// put mark in the map
						if(x && y)
						{
							// Get coordinates
							var point = new GLatLng(parseFloat(x),
													parseFloat(y));

							// Create marker
							var marker = new GMarker(point);

							// Get data and build marker tooltip
							var collection = markers[i].getAttribute("collection");
							if(collection)
								Create_Tooltip(marker, collection);

							// Add marker to the map
							map.addOverlay(marker);
						};
					}
				});
}


window.addEventListener("load", Load_Alerts, false);

map.addEventListener("clearoverlays", Load_Alerts, false);
