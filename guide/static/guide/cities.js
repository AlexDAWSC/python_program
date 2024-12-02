// cities.js

// Create a layer for the cities
var citiesLayer = L.layerGroup();

// Define a custom icon for the city markers
var cityIcon = L.icon({
    iconUrl: 'https://fonts.gstatic.com/s/i/materialicons/apartment/v6/24px.svg',  // Replace with the URL of your custom icon
    iconSize: [32, 32],              // Size of the icon
    iconAnchor: [16, 32],            // Point of the icon that will be over the coordinates
    popupAnchor: [0, -32]            // Adjustment of the popup relative to the icon
});

// Ensure 'citiesData' is available (it was already defined in the template)
citiesData.forEach(function(city) {
    var popupContent = `
        <b>${city.name}</b><br>
        ${city.state}<br>
        <p>${city.description}</p>
    `;

    // Create a marker for the city with the custom icon
    var marker = L.marker([city.latitude, city.longitude], { icon: cityIcon })
        .bindPopup(popupContent)
        .addTo(citiesLayer);
});

// Add the cities layer to the map
citiesLayer.addTo(map);

// Function to create visibility controls for the cities
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

// Add visibility controls for cities
createToggleControl(citiesLayer, 'Cities');
