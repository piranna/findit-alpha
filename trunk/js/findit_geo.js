var geo = google.gears.factory.create('beta.geolocation');

var current_location = null;


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

	LoadAlerts();
}

window.onunload="GUnload()"


function AddAlert(descripcion, latitud, longitud)
{
	GDownloadUrl("alertManager", LoadAlerts,
				"descripcion=" + descripcion + "&latitud=" + latitud + "&longitud=" + longitud);
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
										var point = new GLatLng(parseFloat(markers[i].getAttribute("lat")),
																parseFloat(markers[i].getAttribute("lon")));
										map.addOverlay(new GMarker(point));
									}
								}
					);
}


function UpdatePosition(position)
{
	// Show message (debug)
	alert('Current lat/lon is: ' + position.latitude + ',' + position.longitude);

	// Update map data


	// Update map position
	current_location = new GLatLng(position.latitude, position.longitude);

	// Get location from/to a TextBox
//	geocoder = new GClientGeocoder();
//	geocoder.getLocations(current_location, showAddress)

	// Center map
	map.setCenter(current_location, 13);

	// Set map markers overlay
	LoadAlerts();
}

function handleError(positionError)
{
	alert('Attempt to get location failed: ' + positionError.message);

	if(!current_location)
		current_location = new GLatLng(37.4419, -122.1419);
}

geo.watchPosition(UpdatePosition, handleError, {enableHighAccuracy: true});
//geo.getCurrentPosition(UpdatePosition, handleError, {enableHighAccuracy: true});