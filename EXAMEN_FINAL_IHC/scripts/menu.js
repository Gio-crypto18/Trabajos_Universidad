const services = document.querySelector("#services")
const Portafolio = document.querySelector("#Portafolio")
const Contacto = document.querySelector("#Contacto")
const Inicio = document.querySelector("#Inicio")

/* Menu Services */
services.addEventListener("click", (s) => {
    s.preventDefault();

    const sectionS = document.querySelector(".services");
    sectionS.scrollIntoView({behavior: "smooth"});
})



/* Menu Contacto */
Contacto.addEventListener("click", (c) => {
    c.preventDefault();

    const sectionC = document.querySelector(".Contacto");
    sectionC.scrollIntoView({behavior: "smooth"});
})

/* Menu Inicio */
Inicio.addEventListener("click", (i) => {
    i.preventDefault();

    const sectionI = document.querySelector(".Inicio");
    sectionI.scrollIntoView({behavior: "smooth"});
})