import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AffiliatesView from '../views/AffiliatesView'
import EmployersView from '../views/EmployersView'
import IndependentView from '../views/IndependentView'
import BusinessAdvisorsView from '../views/BusinessAdvisorsView'
import ServiceProvidersView from '../views/ServiceProvidersView'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/affiliates',
    name: 'affiliates',
    component: AffiliatesView
  },
  {
    path: '/employers',
    name: 'employers',
    component: EmployersView
  },
  {
    path: '/independent',
    name: 'independent',
    component: IndependentView
  },
  {
    path: '/businessadvisors',
    name: 'businessadvisors',
    component: BusinessAdvisorsView
  },
  {
    path: '/serviceproviders',
    name: 'serviceproviders',
    component: ServiceProvidersView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
