$(document).ready(function() {

  var kBoardWidth = 8;
  var kBoardHeight= 8;
  var kPieceWidth = 64;
  var kPieceHeight= 64;
  var kPixelWidth = 1 + (kBoardWidth * kPieceWidth);
  var kPixelHeight= 1 + (kBoardHeight * kPieceHeight);
  var numPieza = 0;

  var gCanvasElement = document.getElementById("lienzo");
  var gUIElement = document.getElementById("ui");
  var gDrawingContext = gCanvasElement.getContext("2d");

  function drawBoard() {
     
      gDrawingContext.clearRect(0, 0, kPixelWidth, kPixelHeight);

      gDrawingContext.beginPath();
     
      /* vertical lines */
      for (var x = 0; x <= kPixelWidth; x += kPieceWidth) {
    		gDrawingContext.moveTo(0.5 + x, 0);
    		gDrawingContext.lineTo(0.5 + x, kPixelHeight);
      }
      
      /* horizontal lines */
      for (var y = 0; y <= kPixelHeight; y += kPieceHeight) {
    		gDrawingContext.moveTo(0, 0.5 + y);
    		gDrawingContext.lineTo(kPixelWidth, 0.5 +  y);
      }
      
      /* draw it! */
      gDrawingContext.strokeStyle = "#ccc";
      gDrawingContext.stroke();
      
  }
  function isBusy(x,y){
    return localStorage.getItem(y+","+x);
  }

  function savePieza(x,y,color){
    localStorage.setItem(y+","+x,color);
  }
  //Hacemos que las piezas puedan moverse
  $("div img").draggable({ 
    helper: "clone", //Creamos una copia
    containment: 'canvas', //Solo puede moverse por el lienzo
    cursor: 'move', //Cambiamos el raton
    // when dragging stops
    stop: function(event, ui) {
      var posX = ui.position.left; //posX del usuario
      var posY = ui.position.top; //posY del usuario

      //Obtenemos las coor casilla
      casX = Math.round(posX/kPieceWidth);
      casY = Math.round(posY/kPieceHeight)-1;

      if (isBusy(casX,casY)==null){ //Si la casilla no esta ocupada..
        savePieza(casX,casY,$(this).attr("src"));
        //Indicamos las coordenadas de donde colocar la pieza
        x=(casX*kPieceWidth);
        y=(casY*kPieceHeight);

        //Dibujamos la pieza
        var pieza = document.createElement("img"); //Creamos una pieza
        pieza.setAttribute('src',$(this).attr("src")); //Le decimos a la pieza q sea del mismo color q la seleccionada
        pieza.setAttribute('id','pieza_movida'+numPieza); //Le indicamos un id unico
        pieza.setAttribute('class',$(this).attr("id")); //Le indicamos el tipo de pieza que es
        $('canvas').append(pieza); //La añadimos al canvas
        gDrawingContext.drawImage(pieza,x,y); //La dibujamos
        numPieza++;

        //Escribimos las coordenadas accediendo a la pieza creada
        var elem = document.createElement("LI");
        gUIElement.appendChild(elem);
        elem.innerHTML = pieza.getAttribute('class')+" ("+pieza.getAttribute('id')+") --> "+casY+":"+casX+"<br>";
      }else{
        alert("Casilla ocupada!");
      }
    }
  });

    localStorage.clear(); //Limpiamos localStorage   
    drawBoard();

});

