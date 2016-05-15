/*
Crea una clase Raqueta con los siguientes atributos:
	posX: indica la posición horizontal de la raqueta (una vez fijada, no cambiará)
	posY: indica la posición vertical de la raqueta
	velocidad: un número entero, indica la velocidad vertical de movimiento. Por defecto = 1
y métodos:
	mover() : mueve la raqueta a la posición X,Y (atendiendo a la velocidad)
	incVelocidad(vel): incrementa la velocidad vertical de la raqueta en vel (vel es un número entero)

crea un método pintar() 3 dentro de la clase Raqueta, que toma como parámetro un
contexto 2D para pintar en el canvas. El método pintar crea una línea de anchura 8 y altura
48 desde la posición de la raqueta.
*/
function Raqueta(posX,posY){
	this.posX= posX;
	this.posY = posY;
	this.velocidad = 1;
}
Raqueta.prototype.mover = function(){
	this.posY = this.posY * this.velocidad;
}
Raqueta.prototype.incVelocidad = function(vel){
	this.velocidad = this.velocidad + vel;
}
Raqueta.prototype.pintar = function(contexto){
	contexto.beginPath();
	contexto.lineWidth = 8; //8 a cada lado
	contexto.strokeStyle = "white";
	contexto.moveTo(this.posX,this.posY);
	contexto.lineTo(this.posX,this.posY+48);
	contexto.stroke();

	contexto.fill();
}
Raqueta.prototype = new Raqueta();
Raqueta.prototype.constructor = Raqueta;