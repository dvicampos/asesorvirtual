//FUNCION PARA EL TEXTO
function send_message(message) {
  $.ajax({
    type: "POST",
    url: "/message",
    data: { message: message },
    success: function(response) {
      // $("#chat").html("<div>" + response + "</div>");
      $("#chat").append("<div>"+ response +"</div>");
      console.log("holaaa")
      if (message === 'salir') {
        $("#estado").text('Salio del chat');
      }
      setTimeout(scrollToBottom, 10);
    }
  });
}


function scrollToBottom() {
  window.scrollTo({
    top: window.pageYOffset + 2000,
    behavior: "smooth"
  });
}

const btnenvi = document.querySelector("#btn-enviar");
btnenvi.addEventListener("click", () => {
  btnenvi.style.display = "none";
});

function send() {
  var userinput = document.getElementById("userinput").value;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("chatbox").innerHTML +=
        "<p class='comentarior burbujar'>Hola mi nombre es " + this.responseText + "</p>" + "<p class='comentarios burbuja'>Hola " + this.responseText + " bienvenido <br> Permíteme ayudarte con el tema de la célula y sus componentes</p>";
    }
  };
  xhttp.open("GET", "/get?msg=" + userinput, true);
  xhttp.send();
  document.getElementById("userinput").value = "";
  var caja = document.querySelector(".barram");
  caja.style.display = "none";

  var msje = document.getElementById("mi-mensaje");
  msje.style.display = "block";

}

function ejecutar(){
  
  var userInput = document.getElementById("userinput").value.trim();
  var div = document.getElementById('inicio');
  var text = 'Ingrese un nombre por favor';
    if (userInput === "") {
      div.innerHTML = '<p class="separar comentario burbuja">' + text + '</p>';
      return;
    }else{
      send_message('Comenzar');
      send();
    }
}