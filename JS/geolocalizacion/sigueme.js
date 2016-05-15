var watchId = null;
var map = null;
var ourCoords =  {
	latitude: 47.624851,
	longitude: -122.52099
};
var elevator = new google.maps.ElevationService();
var altitude_coords=null; //Definimos una variable global para que guarde la altitud 
var content="Vacío";

window.onload = obtenerLocalizacion;

function obtenerLocalizacion() {
	if (navigator.geolocation) {
		var botonWatch = document.getElementById("watch");
		botonWatch.onclick = iniciarMonitorizacion;
		var botonClearWatch = document.getElementById("clearWatch");
		botonClearWatch.onclick = detenerMonitorizacion;
	} else {
		alert("No se ha podido acceder al API de geolocalizacion");
	}
}


function mostrarLocalizacion(posicion) {
	var latitude = posicion.coords.latitude;
	var longitude = posicion.coords.longitude;

	var div = document.getElementById("location");
	div.innerHTML = "Tu posición es: Latitud: " + latitude + ", Longitud: " + longitude;
	div.innerHTML += "<br> (con una precisión de " + posicion.coords.accuracy + " metros)";

	if (map == null) {
		mostrarMapa(posicion.coords);
	} else {
		centrarMapa(posicion.coords);
	}
}

function mostrarMapa(coords) {
	altitude_coords = coords.altitude;
	var googleLatAndLong = new google.maps.LatLng(coords.latitude, coords.longitude);
	var mapOptions = {
		zoom: 10,
		center: googleLatAndLong,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var mapDiv = document.getElementById("map");
	map = new google.maps.Map(mapDiv, mapOptions);

	// añadir marcador 
	var title = "Tu geolocalización:";
	content = "Latitud: " + coords.latitude + ", Longitud: " + coords.longitude;
	//Indicamos la latitud y longitud inicial y procedemos a obtener la altitud

	getAltitud(googleLatAndLong); //Obtenemos la altitud

	addMarker(map, googleLatAndLong, title);
}

function centrarMapa(coords) {
	 altitude_coords = coords.altitude;
	 var latitud = coords.latitude;
	 var longitud = coords.longitude;
	 var latlong = new google.maps.LatLng(latitud, longitud);
	 content = "Latitud: " + latitud + ", Longitud: " + longitud; //Actualizamos la longitud y latitud del nuevo lugar
	 getAltitud(latlong); //Obtenemos la nueva altitud
	 map.panTo(latlong);

	 addMarker(map, latlong, "Tu nueva localización"); //El propio getAltitud cargara la altitud
}

function addMarker(map, latlong, title) {
	var markerOptions = {
		position: latlong,
		map: map,
		title: title,
		clickable: true
	};
	var marker = new google.maps.Marker(markerOptions);
	infoWindow.setPosition(latlong); //Colocamos el infowindow

	google.maps.event.addListener(marker, 'click', function() {
		infoWindow.open(map);
	});
}


function mostrarError(error) {
	var errorTypes = {
		0: "Error desconocido",
		1: "Permiso denegado",
		2: "Posición no disponible",
		3: "Tiempo de espera agotado"
	};
	var errorMessage = errorTypes[error.code];
	if (error.code == 0 || error.code == 2) {
		errorMessage = errorMessage + " " + error.message;
	}
	var div = document.getElementById("location");
	div.innerHTML = errorMessage;
}


function iniciarMonitorizacion() {
	watchId = navigator.geolocation.watchPosition(mostrarLocalizacion,mostrarError,  {maximumAge:30000, timeout:5000, enableHighAccuracy:true});
}


function detenerMonitorizacion() {
	if (watchId) {
		navigator.geolocation.clearWatch(watchId);
		watchId = null;
	}
}
var infoWindow = new google.maps.InfoWindow(); 
//Creamos otro infoWindow ya que el método getElevationForLocations es asíncrono, 
//y desde ahí no podriamos editar nuestro propio content
function getAltitud(latAndLong){	

	//Calculamos la altitud
	var locations = [];
	locations.push(latAndLong);
	// Create a LocationElevationRequest object using the array's one value
	var positionalRequest = {
		'locations': locations
	}
	// Initiate the location request
	elevator.getElevationForLocations(positionalRequest, function(results, status) {
		if (status == google.maps.ElevationStatus.OK) {
			// Retrieve the first result
			if (results[0]) {
				if (altitude_coords == null || altitude_coords == 0){
					//Si no existe altitude_coords, o nos da una altitud 0, calculamos la posicion (nº real + 2 digitos)
					result_altitude= parseFloat(results[0].elevation); //Numero real
					result_altitude = result_altitude.toFixed(2); //2 Decimales
					infoWindow.setContent(content + ", Altitud:"+ result_altitude);
				}else{
					//Sino ponemos la que nos da la API de geolocalizacion
					infoWindow.setContent(content + ", Altitud con la API de geolocalizacion:"+ altitude_coords);
				}
									
			} 
		} 	
	});
}
