var files;
function cambiarColor(e){
	dragOver(e);
	e.target.className = "hover"; //Enmarcamos en rojo
}

function gestorFicheros(e){
	
	dragOver(e);
	files = e.dataTransfer.files;
	
	var listado = document.getElementById("listadoFicheros");
	var vacio = document.getElementById("vacio");
	if (vacio){
		listado.removeChild(vacio); //Si es el primer elemento, borramos el comentario de vacio
	}
	for (var i = 0, f; f = files[i]; i++) {
		var elem = document.createElement("LI");
		listado.appendChild(elem);
		elem.innerHTML = "Fichero: "+f.name;
	}
}

function dragOver(e){
	//El evento que le llega lo cancela
	e.stopPropagation();
	e.preventDefault();	
	e.target.className = ""; //borramos el marco al salir
}

function enviar(){
	var formData = new FormData(document.getElementById("uploadform")); 
	for (var i = 0; i < files.length; i++) {
		formData.append('file[]', files[i]);
	}

	// POST via AJAX
	var xhr = new XMLHttpRequest();
	xhr.open('POST', 'upload.php');
	xhr.onload = function () {
		if (xhr.status === 200) {
			console.log('all done: ' + xhr.status);
		} else {
			console.log('blarrghhhhh...');
		}
	};

	xhr.send(formData);
}


var inicializar = function() {

	var dropbox = document.getElementById("dropbox");

	submitbutton = document.getElementById("submitButton");
	submitbutton.onclick = enviar;
	
	dropbox.addEventListener("dragexit", dragOver, false); //Cuando estas arrastrando algo y sales de una capa
	dropbox.addEventListener("dragleave", dragOver, false);
	dropbox.addEventListener("dragover", cambiarColor, false); //Cuando te mueves con algo seleccionado
	dropbox.addEventListener("dragenter", cambiarColor, false); //Cuando estas arrastrando algo y entras en una capa --COLOR ROJO
	dropbox.addEventListener("drop", gestorFicheros, false); //Cuando sueltas un elemento
}

window.onload = inicializar;

