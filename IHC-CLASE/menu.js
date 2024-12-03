const inicio = document.querySelector("#inicio");
const servicios = document.querySelector("#servicios");
const contacto = document.querySelector("#contacto");
const inicioSesion = document.querySelector("#inicios");

// Menu Inicio
inicio.addEventListener("click", (e) => {
    e.preventDefault();
    const sectionInicio = document.querySelector("#Inicio");
    sectionInicio.scrollIntoView({ behavior: "smooth" });
});

// Menu Servicios
servicios.addEventListener("click", (e) => {
    e.preventDefault();
    const sectionServicios = document.querySelector("#servicios");
    sectionServicios.scrollIntoView({ behavior: "smooth" });
});

// Menu Contacto
contacto.addEventListener("click", (e) => {
    e.preventDefault();
    const sectionContacto = document.querySelector("#contacto");
    sectionContacto.scrollIntoView({ behavior: "smooth" });
});

// Menu Inicio de Sesión
inicioSesion.addEventListener("click", (e) => {
    e.preventDefault();
    const sectionInicioSesion = document.querySelector("#inicio_sesion");
    sectionInicioSesion.scrollIntoView({ behavior: "smooth" });
});