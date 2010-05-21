var tooltip;
var current_location = new GLatLng(37.4419, -122.1419);
//var current_location = null;


window.onload = function()
{
	// Create map
	map = new GMap2(document.getElementById("map_canvas"));

	// Enable map controls
	map.addControl(new GMapTypeControl());
	map.addControl(new GLargeMapControl());
	map.addControl(new GScaleControl());
	map.addControl(new GOverviewMapControl());

	map.setCenter(current_location, 2);

// preparar tooltip
	tooltip = document.createElement("div");
	map.getPane(G_MAP_FLOAT_PANE).appendChild(tooltip);
	tooltip.style.visibility="hidden";

	LoadAlerts();
}

window.onunload="GUnload()"


function AddAlert(description, latitud,longitud, collection)
{
	GDownloadUrl("alertManager", LoadAlerts,
				"description=" + description
				+ "&latitud=" + latitud
				+ "&longitud=" + longitud
				+ "&collection=" + collection);
}

// funcion para mostrar el tooltip
function showTooltip(marker)
{
	tooltip.innerHTML = marker.tooltip;
	var point=map.getCurrentMapType().getProjection().fromLatLngToPixel(map.fromDivPixelToLatLng(new GPoint(0,0),true),map.getZoom());
	var offset=map.getCurrentMapType().getProjection().fromLatLngToPixel(marker.getPoint(),map.getZoom());
	var anchor=marker.getIcon().iconAnchor;
	var width=marker.getIcon().iconSize.width;
	var height=tooltip.clientHeight;
	var pos = new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(offset.x - point.x - anchor.x + width, offset.y - point.y -anchor.y -height)); 
	pos.apply(tooltip);
	tooltip.style.visibility="visible";
}

function LoadAlerts()
{
	GDownloadUrl("alertManager", function(data, responseCode)
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
										{
											marker.tooltip = '<div class="tooltip">' + collection +'</div>';
											GEvent.addListener(marker, 'click', function()
																				{
																					marker.openInfoWindowHtml(collection);

																					// ocultar tooltip al hacer click
																					tooltip.style.visibility="hidden";
																				}
																);
											GEvent.addListener(marker,"mouseover", function(){showTooltip(marker);});
											GEvent.addListener(marker,"mouseout", function(){tooltip.style.visibility="hidden";});
										};

										map.addOverlay(marker);
									}
								}
					);
}


//var geo = google.gears.factory.create('beta.geolocation');

//function UpdatePosition(position)
//{
////	// Show message (debug)
////	alert('Current lat/lon is: ' + position.latitude + ',' + position.longitude);

//	// Update map data


//	// Update map position
//	current_location = new GLatLng(position.latitude, position.longitude);

//	// Get location from/to a TextBox
////	geocoder = new GClientGeocoder();
////	geocoder.getLocations(current_location, showAddress)

//	// Center map
//	map.setCenter(current_location, 13);

//	// Set map markers overlay
//	LoadAlerts();
//}

//function handleError(positionError)
//{
//	alert('Attempt to get location failed: ' + positionError.message);

//	if(!current_location)
//		current_location = new GLatLng(37.4419, -122.1419);
//}

//geo.watchPosition(UpdatePosition, handleError, {enableHighAccuracy: true});
