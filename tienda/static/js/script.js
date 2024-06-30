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
var productosEnCarrito = {};

function agregarAlCarrito(nombre, precio, codigo) {
    cantidad += 1;
    document.getElementById("cantidadCarro").innerText = "(" + cantidad + ")";

    if (productosEnCarrito[codigo]) {
        productosEnCarrito[codigo].cantidad += 1;
    } else {
        productosEnCarrito[codigo] = { nombre: nombre, precio: precio, cantidad: 1, imagenUrl: imagenUrl };
    }

    actualizarListaProductos();
    totalPrecio += precio;
    actualizarTotalPrecio();
    mostrarOcultarMensajeCarrito();

    var offcanvas = new bootstrap.Offcanvas(document.getElementById('offcanvasRight'));
    offcanvas.show();
}

function actualizarListaProductos() {
    var contenedorProductos = document.getElementById('listaProductos');
    contenedorProductos.innerHTML = '';  // Limpiar la lista antes de actualizarla

    // for (var codigo in productosEnCarrito) {
    //     var producto = productosEnCarrito[codigo];
    var nuevoProducto = document.createElement('div');
    nuevoProducto.classList.add('producto-en-carrito');
    nuevoProducto.innerHTML = `
        <div class="d-flex justify-content-between align-items-center">
            {% if carro %}
                {% for x in carro %}
                    <p>{{x.nombre}} - $ {{x.precio}} CLP (Cantidad: {{x.cantidad}})</p>
                {% endfor %}
            {% endif %}
        </div>
    `;
    contenedorProductos.appendChild(nuevoProducto);

    totalPrecio += precio;
    actualizarTotalPrecio();
    mostrarOcultarMensajeCarrito();
    }


function actualizarTotalPrecio() {
    document.getElementById("totalPrecio").innerText = "Total: $" + totalPrecio.toFixed(0) + " CLP";
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

function actualizarMensajeCarrito() {
        document.getElementById('mensajeTitulo').innerText = 'Producto agregado al carrito';
        document.getElementById('mensajeTexto').innerText = '¡Agregaste un producto! Continúa comprando o procede al carrito.';
        document.getElementById('mensajeCarrito').style.display = 'block';
    }