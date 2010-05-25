function Make_Icon()
{
	var icon = new GIcon();
	icon.image = "http://www.google.com/mapfiles/turkey.png";
	icon.shadow = "http://www.google.com/mapfiles/turkeyshadow.png";
	icon.iconSize = new GSize(59, 62);
	icon.shadowSize = new GSize(91, 62);
	icon.iconAnchor = new GPoint(37, 59);
	icon.infoWindowAnchor = new GPoint(31, 8);

	return icon;
}

function Load_Incidencias()
{
	GDownloadUrl("/xml/incidenciasXY.xml",
//	GDownloadUrl("http://dgt.es/incidenciasXY.xml",
				function(data, responseCode)
				{
					// Get incidencias
					var xml = GXml.parse(data);
					var incidencias = xml.documentElement.getElementsByTagName("incidencia");

					// for every incidencia,
					// get it's coordinates and put mark in the map
					for(var i = 0; i<incidencias.length; i++)
					{
						// Get x and y coordinates
						var x = null;
						var y = null;

						var childrens = incidencias[i].childNodes;
						for(var j = 0;
							j<childrens.length && !(x && y);
							j++)
						{
							var child = childrens[j];

							if(child.nodeName=="x" && child.childNodes[0])
								x = child.childNodes[0].nodeValue;

							else if(child.nodeName=="y" && child.childNodes[0])
								y = child.childNodes[0].nodeValue;
						};

						// If we have get x and y coordinates,
						// put mark in the map
						if(x && y)
						{
							// Get coordinates
							var point = new GLatLng(parseFloat(x),
													parseFloat(y));

							// Get data and build marker tooltip

							// Create marker
							var marker = new GMarker(point, Make_Icon());

							// Add marker to the map
							map.addOverlay(marker);
						};
					}
				})
};


window.addEventListener("load", Load_Incidencias, false);

map.addEventListener("clearoverlays", Load_Incidencias, false);
