<template>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      
      <title>Health Company</title>

      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@200;400&family=Volkhov:wght@700&display=swap" rel="stylesheet">
    </head>
    <nav>
      <router-link to="/">Inicio</router-link>
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>

  </html>
</template>

<style>
/*Global*/
:root {
    --primaryFont: 'Poppins', sans-serif;
    --secondaryFont: 'Volkhov', serif;

    --font1: rgb(28, 28, 33);
    --selectedFont1: #1f1f1f;
    --background1: #BFBFBF;
    --background2: #E6C999;
}

* {
  margin: 0;
  padding: 0;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.important {
  color: var(--font1);
  padding-left: 20px;
  padding-right: 20px;
}

.important:hover {
  color: var(--selectedFont1);
}

.icon {
  color: var(--font1);
}

.icon:hover {
  color: var(--selectedFont1);
  margin-right: -15px;
}

.social-icons {
  position:fixed;
  left: 5px; /* Ajusta la posición horizontalmente */
  top: 50%; /* Ajusta la posición verticalmente */
  z-index:2000;
  transform: translate(0, -50%); /* Centra verticalmente */
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.social-icons a {
  -webkit-transition: all 500ms ease;
  -o-transition: all 500ms ease;
  transition: all 500ms ease;
}
</style>
