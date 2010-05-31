var geo = google.gears.factory.create('beta.geolocation');
var current_location = null;


function UpdatePosition(position)
{
//	// Show message (debug)
//	alert('Current lat/lon is: ' + position.latitude + ',' + position.longitude);

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
