import Vue from "vue";
import App from "./App.vue";
import Router from "vue-router"

import "bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "animate.css";

import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faPlus,
  faMinus,
  faTrash,
  faCheck,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(faPlus, faMinus, faTrash, faCheck);

Vue.component("fa-icon", FontAwesomeIcon);

Vue.use(Router);

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/register", component: Register }
];

const router = new Router({
  routes
});

Vue.config.productionTip = false;

new Vue({
  render: (h) => h(App),
}).$mount("#app");
