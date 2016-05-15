var municipio; //variable global para guardar el municipio seleccionado
var diasSemana; //variable global para guardar los dias de los que vamos a hacer la predicción

//Obtenemos el tiempo de la API
function obtenerTiempo(){
    //fORMATO json, Unidad: metrica, Predección 3 dias, Idioma castellano
    var direccion = "http://api.openweathermap.org/data/2.5/forecast/daily?q="+municipio+"&mode=json&units=metric&cnt=3&lang=sp";
    
     $.ajax({url:direccion,success:function(result){
         mostrarTiempo(result);
     }, error:function(request,error){
            alert("Error: "+ error);
        }
    });
}

//Mostramos el tiempo en nuestro HTML
function mostrarTiempo(data){

	console.log(data);
    $('h3').html("Municipio seleccionado: <b>"+municipio + "</br>");
    
    var infoDia = "";
    //PRECONDICION - SIEMPRE se va a predecir únicamente de 3 dias
    for (var i=0; i<3;i++){
        infoDia+="<b>"+diasSemana[i]+": </b>";
        infoDia+=data.list[i].weather[0].main + " (" + data.list[i].weather[0].description
            +"). Temperatura Mín. " +data.list[i].temp.min +"º. Temperatura Máx. " +data.list[i].temp.max+"º </br>";
    }
    $('#weather').html(infoDia);
}

//Inicializamos
var cargarGestores = function(){
	var combobox = document.getElementById("comboboxCiudad");
	var btn = document.getElementById("btnTiempo");
    diasSemana=["Hoy","Mañana", "Pasado mañana"];

    //Añadimos el evento para cuando pulse el boton
	btn.addEventListener('click', function(){obtenerTiempoMunicipio()});
	
	obtenerTiempoMunicipio(); //Para la primera vez que carga la página

	function obtenerTiempoMunicipio(){  //función para cada vez q se clicke en el botón.
		//Cuando clickamos sobre el boton, calculamos el tiempo
		municipio = combobox.options[combobox.selectedIndex].text; //Actualizamos la variable
		obtenerTiempo();
	}
}
window.onload = cargarGestores;

