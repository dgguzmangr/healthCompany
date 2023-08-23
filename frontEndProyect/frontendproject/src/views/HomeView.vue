<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-12">
        <MainNav/>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <SectionNav/>
      </div>
    </div>
    <div class="row">
      <div class="col-12 h-50 bg-primary">
        <SlidePrueba/>
      </div>
    </div>
    <div class=" row">
      <div class="col-1 h-100">
        <SocialNetworks/>
      </div>
      <div class="container-fluid col-12 bg-info d-flex flex-column" style="height: 160px;">
        <h2>main post</h2>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <FooterSection/>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MainNav from '@/components/MainNav.vue'
import SectionNav from '@/components/SectionNav.vue'
import SlidePrueba from '@/components/SlidePrueba.vue'
import SocialNetworks from '@/components/SocialNetworks.vue'
import FooterSection from '@/components/FooterSection.vue'

export default {
  name: 'HomeView',
  components: {
    MainNav,
    SectionNav,
    SlidePrueba,
    SocialNetworks,
    FooterSection,
  }
}
</script>
<style>
</style>
