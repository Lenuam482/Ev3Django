$(document).ready(function(){
    $("#registroForm").submit(function(event){

        event.preventDefault();
        

        var usuario = $("#usuario").val();
        var contraseña = $("#contraseña").val();
        var verificarcontra = $("#verificarcontra").val();

        if(usuario.length < 5 || usuario.length > 15){
            alert("El nombre de usuario debe tener entre 5 y 15 caracteres.");
            return;
        }

        if(contraseña.length < 8 || contraseña.length > 15){
            alert("La contraseña debe tener entre 8 y 15 caracteres.");
            return;
        }

        if(verificarcontra !== contraseña){
            alert("Las contraseñas deben coincidir.");
            return;
        }


        alert("¡Registro exitoso!");
        document.getElementById("registroForm").reset();
    });
    
});

var cantidad = 0;
var totalPrecio = 0;

function agregarAlCarrito(nombre, precio) {

    cantidad = cantidad + 1;

    document.getElementById("cantidadCarro").innerText = "(" + cantidad + ")";

    var nuevoProducto = document.createElement('div');
    nuevoProducto.innerHTML = '<p>' + nombre + ' - $' + precio + " CLP" + '</p>';

    var contenedorProductos = document.getElementById('listaProductos');
    contenedorProductos.appendChild(nuevoProducto);

    totalPrecio = totalPrecio + precio;

    actualizarTotalPrecio();

    mostrarOcultarMensajeCarrito();

    var offcanvas = new bootstrap.Offcanvas(document.getElementById('offcanvasRight'));
    offcanvas.show();
}

function actualizarTotalPrecio() {

    document.getElementById("totalPrecio").innerText = "$" + totalPrecio.toFixed(0) + " CLP";
}

function mostrarOcultarMensajeCarrito() {
    var mensajeCarrito = document.getElementById('mensajeCarrito');
    if (cantidad > 0) {
        mensajeCarrito.style.display = "none";
    } else {
        mensajeCarrito.style.display = "block";
    }
}

document.addEventListener('DOMContentLoaded', function() {
    mostrarOcultarMensajeCarrito();
});