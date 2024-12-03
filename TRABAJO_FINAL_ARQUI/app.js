
//Variable que mantiene el estado visible del carrito
var carritoVisible = false;

//Espermos que todos los elementos de la pàgina cargen para ejecutar el script
if(document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
}else{
    ready();
}

function ready(){
    
    //Agregremos funcionalidad a los botones eliminar del carrito
    var botonesEliminarItem = document.getElementsByClassName('btn-eliminar');
    for(var i=0;i<botonesEliminarItem.length; i++){
        var button = botonesEliminarItem[i];
        button.addEventListener('click',eliminarItemCarrito);
    }

    //Agrego funcionalidad al boton sumar cantidad
    var botonesSumarCantidad = document.getElementsByClassName('sumar-cantidad');
    for(var i=0;i<botonesSumarCantidad.length; i++){
        var button = botonesSumarCantidad[i];
        button.addEventListener('click',sumarCantidad);
    }

     //Agrego funcionalidad al buton restar cantidad
    var botonesRestarCantidad = document.getElementsByClassName('restar-cantidad');
    for(var i=0;i<botonesRestarCantidad.length; i++){
        var button = botonesRestarCantidad[i];
        button.addEventListener('click',restarCantidad);
    }

    //Agregamos funcionalidad al boton Agregar al carrito
    var botonesAgregarAlCarrito = document.getElementsByClassName('boton-item');
    for(var i=0; i<botonesAgregarAlCarrito.length;i++){
        var button = botonesAgregarAlCarrito[i];
        button.addEventListener('click', agregarAlCarritoClicked);
    }

    //Agregamos funcionalidad al botón comprar
    document.getElementsByClassName('btn-pagar')[0].addEventListener('click',pagarClicked)
}
//Eliminamos todos los elementos del carrito y lo ocultamos
function pagarClicked(){
    // Guardar el resumen del carrito en localStorage
    var carritoItems = document.getElementsByClassName('carrito-items')[0];
    var items = [];
    for (var i = 0; i < carritoItems.children.length; i++) {
        var item = carritoItems.children[i];
        var titulo = item.getElementsByClassName('carrito-item-titulo')[0].innerText;
        var precio = item.getElementsByClassName('carrito-item-precio')[0].innerText;
        var cantidad = item.getElementsByClassName('carrito-item-cantidad')[0].value;
        items.push({ titulo, precio, cantidad });
    }
    localStorage.setItem('resumenCarrito', JSON.stringify(items));
    
    // Redireccionar a la página de pago
    window.location.href = "pago.html";
}

//Funciòn que controla el boton clickeado de agregar al carrito
function agregarAlCarritoClicked(event){
    var button = event.target;
    var item = button.parentElement;
    var titulo = item.getElementsByClassName('titulo-item')[0].innerText;
    var precio = item.getElementsByClassName('precio-item')[0].innerText;
    var imagenSrc = item.getElementsByClassName('img-item')[0].src;
    console.log(imagenSrc);

    agregarItemAlCarrito(titulo, precio, imagenSrc);

    hacerVisibleCarrito();
}

//Funcion que hace visible el carrito
function hacerVisibleCarrito(){
    carritoVisible = true;
    var carrito = document.getElementsByClassName('carrito')[0];
    carrito.style.marginRight = '0';
    carrito.style.opacity = '1';

    var items =document.getElementsByClassName('contenedor-items')[0];
    items.style.width = '60%';
}

//Funciòn que agrega un item al carrito
function agregarItemAlCarrito(titulo, precio, imagenSrc){
    var item = document.createElement('div');
    item.classList.add = ('item');
    var itemsCarrito = document.getElementsByClassName('carrito-items')[0];

    //controlamos que el item que intenta ingresar no se encuentre en el carrito
    var nombresItemsCarrito = itemsCarrito.getElementsByClassName('carrito-item-titulo');
    for(var i=0;i < nombresItemsCarrito.length;i++){
        if(nombresItemsCarrito[i].innerText==titulo){
            alert("El item ya se encuentra en el carrito");
            return;
        }
    }

    var itemCarritoContenido = `
        <div class="carrito-item">
            <img src="${imagenSrc}" width="80px" alt="">
            <div class="carrito-item-detalles">
                <span class="carrito-item-titulo">${titulo}</span>
                <div class="selector-cantidad">
                    <i class="fa-solid fa-minus restar-cantidad"></i>
                    <input type="text" value="1" class="carrito-item-cantidad" disabled>
                    <i class="fa-solid fa-plus sumar-cantidad"></i>
                </div>
                <span class="carrito-item-precio">${precio}</span>
            </div>
            <button class="btn-eliminar">
                <i class="fa-solid fa-trash"></i>
            </button>
        </div>
    `
    item.innerHTML = itemCarritoContenido;
    itemsCarrito.append(item);

    //Agregamos la funcionalidad eliminar al nuevo item
     item.getElementsByClassName('btn-eliminar')[0].addEventListener('click', eliminarItemCarrito);

    //Agregmos al funcionalidad restar cantidad del nuevo item
    var botonRestarCantidad = item.getElementsByClassName('restar-cantidad')[0];
    botonRestarCantidad.addEventListener('click',restarCantidad);

    //Agregamos la funcionalidad sumar cantidad del nuevo item
    var botonSumarCantidad = item.getElementsByClassName('sumar-cantidad')[0];
    botonSumarCantidad.addEventListener('click',sumarCantidad);

    //Actualizamos total
    actualizarTotalCarrito();
}
//Aumento en uno la cantidad del elemento seleccionado
function sumarCantidad(event){
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    console.log(selector.getElementsByClassName('carrito-item-cantidad')[0].value);
    var cantidadActual = selector.getElementsByClassName('carrito-item-cantidad')[0].value;
    cantidadActual++;
    selector.getElementsByClassName('carrito-item-cantidad')[0].value = cantidadActual;
    actualizarTotalCarrito();
}
//Resto en uno la cantidad del elemento seleccionado
function restarCantidad(event){
    var buttonClicked = event.target;
    var selector = buttonClicked.parentElement;
    console.log(selector.getElementsByClassName('carrito-item-cantidad')[0].value);
    var cantidadActual = selector.getElementsByClassName('carrito-item-cantidad')[0].value;
    cantidadActual--;
    if(cantidadActual>=1){
        selector.getElementsByClassName('carrito-item-cantidad')[0].value = cantidadActual;
        actualizarTotalCarrito();
    }
}

//Elimino el item seleccionado del carrito
function eliminarItemCarrito(event){
    var buttonClicked = event.target;
    buttonClicked.parentElement.parentElement.remove();
    //Actualizamos el total del carrito
    actualizarTotalCarrito();

    //la siguiente funciòn controla si hay elementos en el carrito
    //Si no hay elimino el carrito
    ocultarCarrito();
}
//Funciòn que controla si hay elementos en el carrito. Si no hay oculto el carrito.
function ocultarCarrito(){
    var carritoItems = document.getElementsByClassName('carrito-items')[0];
    if(carritoItems.childElementCount==0){
        var carrito = document.getElementsByClassName('carrito')[0];
        carrito.style.marginRight = '-100%';
        carrito.style.opacity = '0';
        carritoVisible = false;
    
        var items =document.getElementsByClassName('contenedor-items')[0];
        items.style.width = '100%';
    }
}
//Actualizamos el total de Carrito
function actualizarTotalCarrito(){
    //seleccionamos el contenedor carrito
    var carritoContenedor = document.getElementsByClassName('carrito')[0];
    var carritoItems = carritoContenedor.getElementsByClassName('carrito-item');
    var total = 0;
    //recorremos cada elemento del carrito para actualizar el total
    for(var i=0; i< carritoItems.length;i++){
        var item = carritoItems[i];
        var precioElemento = item.getElementsByClassName('carrito-item-precio')[0];
        //quitamos el simobolo peso y el punto de milesimos.
        var precio = parseFloat(precioElemento.innerText.replace('S/ ',''));
        var cantidadItem = item.getElementsByClassName('carrito-item-cantidad')[0];
        console.log(precio);
        var cantidad = cantidadItem.value;
        total = total + (precio * cantidad);
    }
    total = Math.round(total * 100)/100;

    document.getElementsByClassName('carrito-precio-total')[0].innerText = 'S/ '+total.toLocaleString("es");

}

// app.js (Node.js + Express)
const express = require('express');
const app = express();
const PORT = 3000;

// Simulamos la base de datos
const usuariosDB = {
    '123': { nombre: 'Juan Pérez' } // Aquí irían los datos de los usuarios
};

// Endpoint para obtener el nombre del usuario
app.get('/api/usuario', (req, res) => {
    // Aquí puedes usar el ID del usuario para buscar en la base de datos
    const userID = '123'; // Reemplaza con el ID actual del usuario autenticado
    const usuario = usuariosDB[userID];

    if (usuario) {
        res.json(usuario);
    } else {
        res.status(404).json({ error: 'Usuario no encontrado' });
    }
});

app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});

        document.addEventListener('DOMContentLoaded', function() {
            // Obtener y mostrar el resumen del carrito almacenado en localStorage
            var resumenCarrito = JSON.parse(localStorage.getItem('resumenCarrito')) || [];
            var resumenDiv = document.getElementById('resumen-carrito');
            var totalCompra = document.getElementById('total-compra');

            function actualizarResumen() {
                resumenDiv.innerHTML = '';
                var total = 0;

                resumenCarrito.forEach((item, index) => {
                    var itemDiv = document.createElement('div');
                    itemDiv.classList.add('item-carrito');
                    itemDiv.innerHTML = `
                        <div class="item-detalle">
                            <img src="${item.imagen}" alt="${item.titulo}" width="50">
                            <div>
                                <p><strong>${item.titulo}</strong></p>
                                <div style="display: flex; align-items: center;">
                                    <button class="boton-cantidad boton-decremento" data-index="${index}">−</button>
                                    <span style="margin: 0 10px;">${item.cantidad}</span>
                                    <button class="boton-cantidad boton-incremento" data-index="${index}">+</button>
                                    <span style="margin-left: 10px;">S/ ${item.precio}</span>
                                </div>
                            </div>
                        </div>
                        <button class="boton-eliminar" data-index="${index}">
                            <img src="icono-basura.png" alt="Eliminar" width="20">
                        </button>
                    `;
                    resumenDiv.appendChild(itemDiv);

                    // Calcular el total acumulado
                    total += parseFloat(item.precio) * item.cantidad;
                });

                // Mostrar el total
                totalCompra.textContent = `Total: S/ ${total.toFixed(2)}`;

                // Asignar eventos a botones después de generar el HTML
                document.querySelectorAll('.boton-incremento').forEach(boton => {
                    boton.addEventListener('click', function() {
                        cambiarCantidad(parseInt(this.getAttribute('data-index')), 1);
                    });
                });

                document.querySelectorAll('.boton-decremento').forEach(boton => {
                    boton.addEventListener('click', function() {
                        cambiarCantidad(parseInt(this.getAttribute('data-index')), -1);
                    });
                });

                document.querySelectorAll('.boton-eliminar').forEach(boton => {
                    boton.addEventListener('click', function() {
                        eliminarProducto(parseInt(this.getAttribute('data-index')));
                    });
                });
            }

            // Cambiar cantidad de productos en el carrito
function cambiarCantidad(index, cantidad) {
    resumenCarrito[index].cantidad = parseInt(resumenCarrito[index].cantidad) + cantidad; // Convertimos a número y luego sumamos/restamos
    if (resumenCarrito[index].cantidad <= 0) {
        resumenCarrito.splice(index, 1);
    }
    localStorage.setItem('resumenCarrito', JSON.stringify(resumenCarrito));
    actualizarResumen();
}

// Eliminar un producto del carrito
function eliminarProducto(index) {
    resumenCarrito.splice(index, 1);
    localStorage.setItem('resumenCarrito', JSON.stringify(resumenCarrito));
    actualizarResumen();
}

// Mostrar el resumen de compra al cargar la página
actualizarResumen();


            // Eliminar un producto del carrito
            function eliminarProducto(index) {
                resumenCarrito.splice(index, 1);
                localStorage.setItem('resumenCarrito', JSON.stringify(resumenCarrito));
                actualizarResumen();
            }

            // Mostrar el resumen de compra al cargar la página
            actualizarResumen();

            // Detectar tipo de tarjeta y mostrar logo
            var numeroTarjetaInput = document.getElementById('numero-tarjeta');
            var logo = document.getElementById('logo-tarjeta');
            
            numeroTarjetaInput.addEventListener('input', function() {
                var numeroTarjeta = this.value;
                if (/^4/.test(numeroTarjeta)) {
                    logo.src = 'visa.png'; // Ruta de imagen de Visa
                } else if (/^5[1-5]/.test(numeroTarjeta)) {
                    logo.src = 'mastercard.png'; // Ruta de imagen de MasterCard
                } else if (/^3[47]/.test(numeroTarjeta)) {
                    logo.src = 'amex.png'; // Ruta de imagen de American Express
                } else if (/^3(?:0[0-5]|[68])/.test(numeroTarjeta)) {
                    logo.src = 'diners_club.png'; // Ruta de imagen de Diners Club
                } else {
                    logo.src = '';
                }
            });

            // Deshabilitar campo de tarjeta si se elige "Efectivo"
            var metodoPagoSelect = document.getElementById('metodo-pago');
            metodoPagoSelect.addEventListener('change', function() {
                if (metodoPagoSelect.value === 'efectivo') {
                    numeroTarjetaInput.disabled = true;
                    numeroTarjetaInput.value = ''; // Limpiar el campo si se elige "Efectivo"
                    logo.src = ''; // Quitar logo de tarjeta
                } else {
                    numeroTarjetaInput.disabled = false;
                }
            });

            // Procesar el formulario y redirigir a la página de confirmación
            var formulario = document.getElementById('formulario-pago');
            formulario.addEventListener('submit', function(event) {
                event.preventDefault();
                var nombre = document.getElementById('nombre').value;
                localStorage.setItem('usuarioRegistrado', nombre);

                alert("Gracias por su compra, " + nombre);
                window.location.href = "index.html"; 
            });
        });
