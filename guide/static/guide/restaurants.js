// restaurants.js

// Create a custom icon for the restaurants
var restaurantIcon = L.icon({
    iconUrl: "https://fonts.gstatic.com/s/i/materialiconsoutlined/restaurant/v16/24px.svg", // Path to the icon image file
    iconSize: [22, 32],  // Size of the icon
    iconAnchor: [16, 32], // The point of the icon that will be at the marker's location
    popupAnchor: [0, -32], // The point where the popup will open
});

// Create a layer for the restaurants
var restaurantsLayer = L.layerGroup();

// Ensure 'restaurantsData' is available (it was already defined in the template)
console.log(restaurantsData);  // Ensure the data is being passed correctly

restaurantsData.forEach(function(restaurant) {
    var popupContent = `
        <b>${restaurant.name}</b><br>
        ${restaurant.state}<br>
        <p>${restaurant.description}</p>
    `;

    // Create a marker with the custom icon
    var marker = L.marker([restaurant.latitude, restaurant.longitude], { icon: restaurantIcon })
        .bindPopup(popupContent)
        .addTo(restaurantsLayer);
});

// Add the restaurants layer to the map
restaurantsLayer.addTo(map);

// Function to create visibility toggle controls for restaurants
function createToggleControl(layer, name) {
    var control = L.control({ position: 'topright' });
    control.onAdd = function() {
        var div = L.DomUtil.create('div', 'leaflet-control-layers leaflet-bar leaflet-control');
        div.innerHTML = `<a href="#" title="Toggle ${name} Visibility" class="leaflet-control-layers-toggle">${name}</a>`;
        div.onclick = function() {
            if (map.hasLayer(layer)) {
                map.removeLayer(layer);
            } else {
                layer.addTo(map);
            }
        };
        return div;
    };
    control.addTo(map);
}

// Add visibility controls for restaurants
createToggleControl(restaurantsLayer, 'Restaurants');
