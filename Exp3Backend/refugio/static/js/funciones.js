
   function Saludar()
   {
     var a = document.getElementById("nombre").value.toUpperCase();
     alert ('Hola! ' + a + ' Bienvenido a Refugio!');
   }


   function Vnumero()
   {
    valor = document.getElementById("fono").value;
    if( isNaN(valor) ) {
      return false;
    }
   }


