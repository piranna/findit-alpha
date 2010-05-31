window.addEventListener("load",
						function()
						{
							// Create map
							map = new GMap2(document.getElementById("map_canvas"));

							// Enable map controls
							map.addControl(new GMapTypeControl());
							map.addControl(new GLargeMapControl());
							map.addControl(new GScaleControl());
							map.addControl(new GOverviewMapControl());

						//	map.setCenter(new GLatLng(35.746512,-7.77832), 5);
							map.setCenter(new GLatLng(37.4419, -122.1419), 2);
						//	map.setCenter(current_location, 2);
						},
						false);

window.onunload="GUnload()";
