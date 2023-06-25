//FUNCION PARA EL TEXTO
// function send_message(message) {
//   $.ajax({
//     type: "POST",
//     url: "/message",
//     data: { message: message },
//     success: function(response) {
//       $("#chat").append("<div>" + response + "</div>");
//       if (message === 'salir') {
//         $("#estado").text('Salio del chat');
//       }
//       setTimeout(scrollToBottom, 10);
//     }
//   });
// }
function send_message(message) {
  $.ajax({
    type: "POST",
    url: "/message",
    data: { message: message },
    success: function(response) {
      $("#chat").html("<div>" + response + "</div>"); // Replace existing content with the response
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

const button = document.querySelector("#mi-boton");
button.addEventListener("click", () => {
  button.style.display = "none";
});
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
        "<p class='comentario burbuja'><strong>AsAD :</strong> " + this.responseText + "</p>";
    }
  };
  xhttp.open("GET", "/get?msg=" + userinput, true);
  xhttp.send();
  document.getElementById("userinput").value = "";
  var caja = document.querySelector(".barram");
  caja.style.display = "none";

  var boton = document.getElementById("mi-boton");
  boton.style.display = "block";

  var msje = document.getElementById("mi-mensaje");
  msje.style.display = "block";
}
