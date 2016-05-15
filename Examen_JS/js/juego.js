$(document).ready(function() {
	var campo;
	var contexto; 
	var margen = 8;
	var bola;
	var raqIzq;
	var raqDcha;
	var reloj;
	var rebotes=0;
	var fin=false;

	function iniciarJuego(canvas) {
		/*
		EJERCICIO 5
		Crea un timer (reloj en JavaScript) para que la bola se mueva por sí misma en el campo
		(atendiendo a su posición y velocidad actual) una vez cada 60 milisegundos.  
		*/
		reloj = setInterval(actualizarBola,60);
		campo = canvas;
		contexto = campo.getContext("2d");
		/*
		EJERCICIO 3
		Instancia la clase bola para generar un objeto bola (como variable global) de 20 pixels de
		radio, blanca, en la posición central del campo.
		*/
		bola = new Bola([campo.width/2,campo.height/2],'#FFFFFF', 20, [0,0]);
		/*
		EJERCICIO 7
		Crea 2 objetos raqueta (raqI, raqD) y sitúalos en pantalla tal y como se indica en este
		*/
		raqIzq = new Raqueta(3,campo.height/2); //3 padding
		raqDcha = new Raqueta(campo.width-3,campo.height/2);

		pintar();
	}

	function pintarCampo() {
		/*
		EJERCICIO 2
		Pinta en pantalla, usando el elemento canvas, el siguiente gráfico (al que llamaremos
		campo de aquí en adelante). El dibujo tiene 600 pixels de ancho y 400 de alto. Hay 3 barras
		verticales blancas: una en el medio del canvas y otras dos en las esquinas (a 8 pixels del
		borde)
		*/
		contexto.clearRect(0,0,campo.width,campo.height);
		
		contexto.fillStyle = "black";
		contexto.fillRect(0,0,campo.width,campo.height);
		contexto.lineWidth = 2;

		//Pintamos las líneas de los Bordes
		contexto.beginPath();
		contexto.moveTo(margen,0);
		contexto.lineTo(margen,campo.height);
		contexto.strokeStyle = "white";
		contexto.stroke();

		contexto.beginPath();
		contexto.moveTo(campo.width-margen,0);
		contexto.lineTo(campo.width-margen,campo.height);
		contexto.strokeStyle = "white";
		contexto.stroke();

		contexto.beginPath();
		contexto.moveTo(campo.width/2,0);
		contexto.lineTo(campo.width/2,campo.height);
		contexto.strokeStyle = "white";
		contexto.stroke();
		
		contexto.fillStyle = "red";
		contexto.font="20px Georgia";
		contexto.fillText("Rebotes: "+rebotes,15,20);
		contexto.fill(); //Relleno
	}

	function pintarRaquetas(){
		raqIzq.pintar(contexto);
		raqDcha.pintar(contexto);
	}

	function pintarBola(){
		/*
		EJERCICIO 3
		Pinta dicha bola en el centro del campo.
		*/
		contexto.fillStyle = bola.color; //defininmos el color de la bola

		contexto.beginPath();
		contexto.arc(bola.posicion[0],bola.posicion[1],bola.radio,0,2*Math.PI);
		contexto.stroke();
		
		contexto.fill(); //Relleno
	}

	function pintar(){
		if (fin == false){ //En el caso de que mantenga la tecla pulsada aun habiendo terminado el juego
			pintarCampo();
			pintarRaquetas();
			pintarBola();
		}
	}

	function actualizarBola(){
		/*
		Ejercicio 4
		En cualquiera de los cuatro casos, una vez cambiada la velocidad, mover() 1 la bola y
		redibujar el campo y la bola (crea una función actualizar() que haga estas tres cosas).
		*/
		colision();
		bola.mover();
		pintar();
	}
	function actualizarRaq(){
		raqIzq.mover();
		raqDcha.mover();
		pintar();
	}

	function savePartida(){
		/*	
		EJERCICIO 9
		Cuando la partida termine, guarda en localStorage el valor de la variable rebotes siempre y
		cuando sea mayor que el valor que ya estuviera guardado (se quiere guardar el mayor
		número de rebotes conseguidos). Escribe en consola tu decisión (por ejemplo, “Guardado
		rebotes=X porque es mayor que rebotes=Y”, donde X es el valor actual de rebotes e Y el
		que había en localStorage).
		*/
		if (localStorage.getItem("rebotes") == null){
			//No hay nada guardado
			localStorage.setItem('rebotes',rebotes);
			console.log("No hay nada guardado, asique guardamos rebotes="+rebotes);
		}else{
			rebotes_guardados= parseInt(localStorage.getItem("rebotes"));
			if (rebotes_guardados<rebotes){
				console.log("Guardado rebotes="+rebotes+" porque es mayor que rebotes="+rebotes_guardados);
				localStorage.setItem('rebotes',rebotes);
			}else{
				console.log("No guardamos porque rebotes="+rebotes+" porque es menor que rebotes="+rebotes_guardados);
			}
		}
	}

	function colision(){
		/*
		EJERCICIO 5
		Modifica el Método actualizar() para que en caso de colisión contra los bordes interiores del campo (los
		que están a 8 pixels de distancia del borde exterior + la parte superior e inferior del campo)
		la bola rebote. 
		*/
		//Actualizamos la posicion para que no rebote
		if (bola.posicion[1]<=20 || bola.posicion[1]>=campo.height-20){ //SUPERIOR O INFERIOR
			bola.cambiarVelocidad([bola.velocidad[0],bola.velocidad[1]*-1]);
		}
		/*
		EJERCICIO 8
		Cambia el método de detección de colisión para que se detecte colisión de la bola con la
		raqueta (la bola rebotará igual que si hubiera una pared). Crea una variable rebotes que se
		incremente cada vez que la bola es golpeada por una raqueta y píntala en pantalla. Si la bola
		toca el borde interior (derecho o izquierdo) desactiva el timer (la bola quedará parada,
		terminando la partida).
		*/
		//RAQUETA 
		else if ( bola.posicion[0]<=(20+margen) || bola.posicion[0]>=campo.width-(20+margen)){ //IZQUIERDA O DERECHA 
			if ((raqIzq.posY <= bola.posicion[1] &&  bola.posicion[1] <=raqIzq.posY+48)
				|| (raqDcha.posY <= bola.posicion[1] &&  bola.posicion[1] <=raqDcha.posY+48)){
				bola.cambiarVelocidad([bola.velocidad[0]*-1,bola.velocidad[1]]);
				rebotes++;
			}else{
				clearInterval(reloj);
				console.log("FIN");
				fin=true;
				savePartida();
			}
		}
	}
	//EVENTO TECLADO
	$(document).keydown(function(e){
		/*
		Ejercicio 4
		Gestiona un evento para detectar las pulsaciones de las teclas de flecha del teclado (arriba,
		abajo, izquierda derecha). 
		Cuando el usuario pulse arriba o abajo, cambiar la velocidad[1] del objeto bola.
		Cuando el usuario pulse izquierda o derecha, cambiar la velocidad[0] del objeto bola.
		*/

		if (fin == false){
			//BOLA: 37 - left, 38 - up, 39 - right, 40 - down
		    if (e.keyCode == 37) {  //IZQUIERDA
		    	bola.cambiarVelocidad([bola.velocidad[0]-1,bola.velocidad[1]]);
				actualizarBola();
			}
		    else if(e.keyCode == 39) {  ///DERECHA
		    	bola.cambiarVelocidad([bola.velocidad[0]+1,bola.velocidad[1]]);
				actualizarBola();
			}
			else if(e.keyCode == 38) {  ///ARRIBA
		    	bola.cambiarVelocidad([bola.velocidad[0],bola.velocidad[1]-1]);
				actualizarBola();
			}
			else if(e.keyCode == 40) {  ///ABAJO
		    	bola.cambiarVelocidad([bola.velocidad[0],bola.velocidad[1]+1]);
				actualizarBola();
			}

			/*
			EJERCICIO 7
			La raqueta izquierda se debe poder mover con las letras Q (arriba) y A (abajo)
			La raqueta derecha se debe poder mover con las letras P (arriba) y L (abajo)
			(para poder reutilizar el mismo código de gestión de teclado del ejercicio 4, en este
			ejercicio sólo se podrá mover una raqueta a la vez)
			*/
			//RAQUETA IZQUIERDA: 81 UP, 65 DOWN 
			else if (e.keyCode == 81){
				raqIzq.posY=raqIzq.posY+1;
				actualizarRaq();
			}
			else if (e.keyCode == 65){
				raqIzq.posY=raqIzq.posY-1;
				actualizarRaq();
			}
			//RAQUETA DCHA: 80 UP, 76 DOWN
			else if (e.keyCode == 80){
				raqDcha.posY= raqDcha.posY-1;
				actualizarRaq();
			}
			else if (e.keyCode == 76){
				raqDcha.posY= raqDcha.posY+1;
				actualizarRaq();
			}
		}
	});

	function adivinar(pos){
		/*
		EJERCICIO 6
		El servidor ha pensado en una posición de la Bola (una posición [x,y]). Tu objetivo es
		adivinar qué posición ha pensado el servidor. Para ello, debes comunicarte con un método
		(de nombre adivinar(posicion) ) que envíe vía AJAX (por método POST ) la posición de la
		bola que tú creas que el servidor ha pensado. El servidor espera un string con formato JSON
		de nombre “mensaje”. El objeto JSON debe contener dos atributos: nombre (tu
		identificador LDAP) y posición. Por ejemplo: { 'nombre' : 'scppevaj', 'posicion': [X,Y] }.
		Si recibe una posición correcta el servidor responderá con el string 'correcto'. Si recibe una
		posición incorrecta, responderá con 'incorrecto'. Indica como comentario en el método
		adivinar() cuál es la posición que ha pensado el servidor.


		No he podido averiguar el número, pero tampoco sé que es lo que falla
		*/
		// POST via AJAX
		var xhr = new XMLHttpRequest();
		var url = "http://188.226.176.242/dawe/rebotes.php";
		var mensaje = JSON.stringify({'nombre':'tperez020','posicion':pos}); //Convertimos el JSON en String;

		xhr.open('POST', url,true);
		xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		xhr.onload = function () {
			console.log(xhr.responseText);
			if (xhr.status == 200 && xhr.responseText == "correcto"){
	       			console.log("Posición averiguada: "+pos);
			}
		};
		xhr.send(mensaje);
	}

	iniciarJuego(document.getElementById('campo'));
});
