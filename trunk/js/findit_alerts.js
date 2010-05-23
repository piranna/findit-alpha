function AddAlert(description, latitud,longitud, collection)
{
	GDownloadUrl("alertManager", LoadAlerts,
				"description=" + description
				+ "&latitud=" + latitud
				+ "&longitud=" + longitud
				+ "&collection=" + collection);
}

function LoadAlerts()
{
	GDownloadUrl("alertManager",
				function(data, responseCode)
				{
					var xml = GXml.parse(data);
					var markers = xml.documentElement.getElementsByTagName("marker");

					map.clearOverlays();

					for(var i = 0; i < markers.length; i++)
					{
						var point = new GLatLng(parseFloat(markers[i].getAttribute("latitud")),
												parseFloat(markers[i].getAttribute("longitud")));

						var marker = new GMarker(point);

						var collection = markers[i].getAttribute("collection");
						if(collection)
							Create_Tooltip(marker, collection);

						map.addOverlay(marker);
					}
				});
}


window.addEventListener("load", LoadAlerts);
