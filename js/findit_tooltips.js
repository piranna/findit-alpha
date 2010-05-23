var tooltip = null;


// funcion para mostrar el tooltip
function showTooltip(marker)
{
	tooltip.innerHTML = marker.tooltip;
	var point=map.getCurrentMapType().getProjection().fromLatLngToPixel(map.fromDivPixelToLatLng(new GPoint(0,0),true),map.getZoom());
	var offset=map.getCurrentMapType().getProjection().fromLatLngToPixel(marker.getPoint(),map.getZoom());
	var anchor=marker.getIcon().iconAnchor;
	var width=marker.getIcon().iconSize.width;
	var height=tooltip.clientHeight;
	var pos = new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(offset.x - point.x - anchor.x + width,
																offset.y - point.y - anchor.y - height)); 
	pos.apply(tooltip);
	tooltip.style.visibility="visible";
}

function Create_Tooltip(marker, collection)
{
	marker.tooltip = '<div class="tooltip">' + collection +'</div>';
	GEvent.addListener(marker,'click', function()
										{
											marker.openInfoWindowHtml(collection);

											// ocultar tooltip al hacer click
											tooltip.style.visibility="hidden";
										}
						);
	GEvent.addListener(marker,"mouseover", function(){showTooltip(marker);});
	GEvent.addListener(marker,"mouseout", function(){tooltip.style.visibility="hidden";});
}


window.addEventListener("load",
						function()
						{
						// preparar tooltip
							tooltip = document.createElement("div");
							map.getPane(G_MAP_FLOAT_PANE).appendChild(tooltip);
							tooltip.style.visibility="hidden";
						});
