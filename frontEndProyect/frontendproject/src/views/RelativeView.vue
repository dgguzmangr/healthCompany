<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12">
                <MainNav/>
            </div>
        </div>
        <div class="row">
            <div class="col-1">
                <SocialNetworks/>
            </div>
            <div class="col-1">
                <LayoutPatient/>
            </div>
            <div class="col-10" style="background-color: var(--dashboard);">
                <div><h3>NÚMERO DE HISTORIA CLÍNICA</h3></div>
                <router-view></router-view>
            </div>
        </div>
        <div class="row">
            <FooterSection/>
        </div>
    </div>
</template>
  
<script>
    // @ is an alias to /src
    import MainNav from '@/components/MainNav.vue'
    import LayoutPatient from '@/components/LayoutPatient.vue'
    import SocialNetworks from '@/components/SocialNetworks.vue'
    import FooterSection from '@/components/FooterSection.vue'
  
  export default {
    name: 'HomeView',
    components: {
        MainNav,
        LayoutPatient,
        SocialNetworks,
        FooterSection,
    }
  }
</script>
  <style>
  </style>