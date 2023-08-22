<template>
    <div class="container-fluid" style="background-color: var(--white);">
      <nav class="navbar navbar-expand-md navbar-light py-1 text-center">
        <div class="col-2">
          <h4>EPS</h4>
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
        <div class="collapse navbar-collapse col-10 justify-content-center" id="navbarNav">
          <ul class="navbar-nav d-flex dflex-wrap  justify-content-md- list-unstyled fw-bold" style="font-family: var(--primaryFont); color: var(--colorB-1);">
            <li><router-link to="/" class="nav-link">INICIO</router-link></li>
            <li><router-link to="/affiliates" class="nav-link">AFILIADOS</router-link></li>
            <li><router-link to="/employers" class="nav-link">EMPLEADORES</router-link></li>
            <li><router-link to="/independent" class="nav-link">INDEPENDIENTES</router-link></li>
            <li><router-link to="/businessadvisors" class="nav-link">ASESORES COMERCIALES</router-link></li>
            <li><router-link to="/serviceproviders" class="nav-link">PRESTADORES DE SERVICIO</router-link></li>
          </ul>
        </div>
      </nav>
    </div>
  </template>