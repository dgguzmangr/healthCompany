<template>
    <div class="container-fluid" style="background-color: var(--background3);">
      <nav class="navbar navbar-expand-md navbar-light py-1 text-center">
        <div class="col-12 col-md-1">
            <img src="@/assets/wing.png" class="img-fluid w-50 logo">
        </div>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse col-md-10 justify-content-center" id="navbarNav">
          <ul class="navbar-nav d-flex dflex-wrap  justify-content-md- list-unstyled fw-bold" style="font-family: var(--primaryFont); color: var(--colorB-1);">
            <li class="px-3 px-md-5"><router-link to="/law" class="nav-link">Ley de transparencia</router-link></li>
            <li class="px-3 px-md-5"><router-link to="/faq" class="nav-link">Preguntas frecuentes</router-link></li>
            <li class="px-3 px-md-5"><router-link to="/pqrs" class="nav-link">Escríbenos tus PQRS</router-link></li>
            <li class="px-3 px-md-5"><router-link to="/requestpassword" class="nav-link">Solicitar clave</router-link></li>
          </ul>
        </div>

        <div class="dropdown col-12 col-md-1 mt-3 mt-md-0 text-center text-md-end">
            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">
                INICIAR SESIÓN
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <li class="dropdown-item"><router-link to="/patient" class="nav-link">Paciente</router-link></li>
                <li class="dropdown-item"><router-link to="/relative" class="nav-link">Familiar designado</router-link></li>
                <li><a class="dropdown-item" href="#">Familiar designado</a></li>
                <li><a class="dropdown-item" href="#">Médico</a></li>
                <li><a class="dropdown-item" href="#">Enfermera/o</a></li>
                <li class="dropdown-item"><router-link to="/assistant" class="nav-link">Asistente</router-link></li>
                <li class="dropdown-item"><router-link to="/admin" class="nav-link">Administrador</router-link></li>
            </ul>
        </div>
      </nav>
    </div>
</template>
