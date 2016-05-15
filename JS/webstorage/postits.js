/* postits.js
 *
 */
window.onload = init;

function init() {

	var button = document.getElementById("add_button");
	button.onclick = createSticky;

	var buttonDelete = document.getElementById("delete_button");
	buttonDelete.onclick = clearStickyNotes;

	// EJERCICIO A
	// cargar las notas postit de localStorage  
	// cada nota se guarda como un par así: postit_X = texto_de_la_nota
	// donde X es el número de la nota
	// por cada una de ellas, llamar al método
	// addStickyToDOM(texto_de_la_nota);
	for (var i=0; i<localStorage.length; i++){
		addStickyToDOM(localStorage.getItem("postit_" + i));
	}
}

function createSticky() {
	var value = document.getElementById("note_text").value;
	
	// EJERCICIO B
        // crear la nota con nombre postit_X, donde X es un número entero
	// (postit_1, postit_2, ...)  y guardarla en el localStorage

	//CREAMOS LA NOTA
	var num_postit = localStorage.length;
	localStorage.setItem("postit_" + num_postit, value); 
	
	//BORRAMOS EL TEXTO DEL INPUT
	document.getElementById("note_text").value = "";

	//AÑADIMOS EL POSTIT
	addStickyToDOM(value);
}


function addStickyToDOM(value) {
	var stickies = document.getElementById("stickies");
	var postit = document.createElement("li");
	var span = document.createElement("span");
	span.setAttribute("class", "postit");
	span.innerHTML = value;
	postit.appendChild(span);
	stickies.appendChild(postit);
}

function clearStickyNotes() {
	// EJERCICIO C
	// Crear un nuevo botón en la ventana de postit notes que al pulsarlo,
	// elimine las notas de pantalla y de localStorage
	// Algoritmo:	
	// obtener una referencia a la capa "stickies"
	// recorrer los hijos (childNodes) de esa referencia,
	// eliminándolos uno a uno (removeChild)
	padre = document.getElementById("stickies");
	while (padre.childElementCount>0){ //Mientras haya elementos..
		padre.removeChild(padre.childNodes[padre.childElementCount]);
	}
	localStorage.clear();
}
