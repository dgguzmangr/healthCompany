<template>
    <footer class="footer py-4">
        <div class="footer__main_container py-2">
            <div class="container">
                <img class="icon py-1" src="@/assets/location-pin.png">
                <h5>Nuestas oficinas</h5>
                <p>Calle 43 # 12-15</p>
                <p>Transversal 94 # 45-12</p>
            </div>
            <div class="container">
                <img class="icon py-1" src="@/assets/support.png">
                <h5>Líneas de atención</h5>
                <p>01 8000 66 66 66 </p>
                <p> Bogotá +57 654 878 2565</p>
            </div>
            <div class="container">
                <img class="icon py-1" src="@/assets/virus.png">
                <h5>Línea Covid-19/ Viruela Símica</h5>
                <p>01 8000 11 22 33 </p>
                <p> Bogotá +57 456 878 2565</p>
            </div>
        </div>
        <div class= "footer__links_recomendations py-3"> 
            <p>2022 © Todos los derechos reservados ǀ Términos y condiciones ǀ Políticas de privacidad ǀ Lineamientos de seguridad ǀ Sostenibilidad</p>
            <p>Navegadores recomendados: Internet Explorer 10.0 o superior; Google Chrome, Firefox o Safari en su última versión</p>
        </div>
        <div class="developers">
            <p><h5>©2023 DGGUZMANGR Developer</h5></p>
        </div>
    </footer>
</template>

<style>
:root {
    --fuenteHeading: 'PT Sans', sans-serif;
    --fuenteParrafos: 'Open Sans', sans-serif;

    --primario: #784D3C;
    --gris: #e1e1e1;
    --blanco: #ffffff;
    --negro: #000000;
} 


h1, h2, h3, h4, h5 {
    font-family: var(--fuenteHeading);
    line-height: 1.2;
}

p {
    font-family: var(--fuenteParrafos);
    line-height: 0.8;
}

/** footer **/
.footer {
    padding-bottom: 1rem;
    margin-top: 4rem;
    width: min(100%, 120rem);
    margin: 0 auto;
}
.footer__main_container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    text-align: center;
    background-color: #ffffff;
}
.container {
    font-size: 1rem;
    line-height: 0;
}
.footer__links_recomendations {
    font-family: var(--fuenteParrafos);
    font-size: 0.8rem;
    line-height: 2;
    text-align: center;
    background-color: gray
}
.icon {
    height: 3rem;
    width: auto; 
    max-height: 100%; 
}
.developers {
    font-family: var(--fuenteParrafos);
    font-size: 0.8rem;
    line-height: 0;
    text-align: center;
}
.developers__members {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
}
</style>