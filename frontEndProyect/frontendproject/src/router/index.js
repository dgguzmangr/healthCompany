import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AffiliatesView from '../views/AffiliatesView'
import EmployersView from '../views/EmployersView'
import IndependentView from '../views/IndependentView'
import BusinessAdvisorsView from '../views/BusinessAdvisorsView'
import ServiceProvidersView from '../views/ServiceProvidersView'
import LawView from '../views/LawView'
import FAQ from '../views/FAQ'
import PQRS from '../views/PQRS'
import RequestPassword from '../views/RequestPassword'
import AssistantView from '../views/AssistantView'
import AssistantPatients from '../views/AssistantPatients'
import AssistantRelative from '../views/AssistantRelative'
import AssistantDoctorsView from '../views/AssistantDoctorsView'
import AssistantNursesView from '../views/AssistantNursesView'
import AdminView from '../views/AdminView'
import AdminUsersView from '../views/AdminUsersView'
import AdminEmployeeView from '../views/AdminEmployeeView'
import PatientView from '../views/PatientView'
import PatientUserView from '../views/PatientUserView'
import PatientVitalSignsView from '../views/PatientVitalSignsView'
import PatientCareTipsView from '../views/PatientCareTipsView'
import PatientDiagnosticView from '../views/PatientDiagnosticView'
import RelativeView from '../views/RelativeView'

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
  {
    path: '/law',
    name: 'law',
    component: LawView
  },
  {
    path: '/faq',
    name: 'faq',
    component: FAQ
  },
  {
    path: '/pqrs',
    name: 'pqrs',
    component: PQRS
  },
  {
    path: '/requestpassword',
    name: 'requestpassword',
    component: RequestPassword
  },
  {
    path: '/assistant',
    name: 'assistant',
    component: AssistantView,
    children: [
      {
        path: '/assistantpatients',
        name: 'assistantpatients',
        component: AssistantPatients
      },
      {
        path: '/assistantrelative',
        name: 'assistantrelative',
        component: AssistantRelative
      },
      {
        path: '/assistantdoctors',
        name: 'assistantdoctors',
        component: AssistantDoctorsView
      },
      {
        path: '/assistantnurses',
        name: 'assistantnurses',
        component: AssistantNursesView
      },
    ]
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminView,
    children: [
      {
        path: '/adminusers',
        name: 'adminusers',
        component: AdminUsersView
      },
      {
        path: '/adminemployee',
        name: 'adminemployee',
        component: AdminEmployeeView
      },
    ]
  },
  {
    path: '/patient',
    name: 'patient',
    component: PatientView,
    children: [
      {
        path: '/patientuser',
        name: 'patientuser',
        component: PatientUserView
      },
      {
        path: '/patientvitalsigns',
        name: 'patientvitalsigns',
        component: PatientVitalSignsView
      },
      {
        path: '/patientcaretips',
        name: 'patientcaretips',
        component: PatientCareTipsView
      },
      {
        path: '/patientdiagnostic',
        name: 'patientdiagnostic',
        component: PatientDiagnosticView
      },
    ]
  },
  {
    path: '/relative',
    name: 'relative',
    component: RelativeView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
