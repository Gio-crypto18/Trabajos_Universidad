const Servicios = document.querySelector("#Servicios");
const Portafolio = document.querySelector("#Portafolio");

Servicios.addEventListener("click", (s) => {
    s.preventDefault();

    const SectionS = document.querySelector(".Servicios");
    SectionS.scrollIntoView({behavior:"smooth"});
});


Portafolio.addEventListener("click", (p) => {
    p.preventDefault();

    const SectionP = document.querySelector(".Portafolio");
    SectionP.scrollIntoView({behavior:"smooth"});
});