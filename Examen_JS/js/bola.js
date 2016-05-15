/*
EJERCICIO 1
Nombre de la clase: Bola
Atributos:
	posición : array de 2 números enteros (representan posiciónX y posiciónY del centro de la bola)
	color: un color en formato RGB (#rrggbb)
	velocidad: array de 2 números enteros (representan incrementoX e incrementoY). Inicialmente velocidad = [0,0]
	aceleración: un número real, inicialmente = 1.0
	radio: número entero, representa el radio de la bola, inicialmente 2.0
Métodos:
	constructor(): asigna los parámetros posición,color, radio, velocidadInicial
	mover(): modifica la posición de la bola (posicion = posición + aceleración * velocidad)
	cambiarVelocidad(velocidad): modifica la velocidad de la bola
*/
function Bola(posicion,color, radio, velocidadInicial){
	this.posicion= posicion;//[posX,posY]
	this.color = color;//RGB
	this.velocidad = velocidadInicial;//[incrementoX,incrementoY]
	this.radio = radio;	
	this.aceleracion = 1.0;
}
Bola.prototype.mover = function(){
	//Eje X y Eje Y
	this.posicion[0] = this.posicion[0] + this.velocidad[0]*this.aceleracion;
	this.posicion[1] = this.posicion[1] + this.velocidad[1]*this.aceleracion;
}
Bola.prototype.cambiarVelocidad = function(velocidadN){
	this.velocidad = velocidadN;
}
Bola.prototype = new Bola();
Bola.prototype.constructor = Bola;