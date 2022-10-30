import { createRouter, createWebHistory } from "vue-router";
import Task from "@/views/main/Task.vue";
import Home from "@/views/main/Home.vue";
import SignInView from "@/views/user/SignIn.vue";
import SignUpView from "@/views/user/SignUp.vue";

const routes = [
  {
    path: "/task/:id?",
    name: "Task",
    component: Task,
  },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/signin",
    name: "SignIn",
    component: SignInView,
  },
  {
    path: "/signup",
    name: "SignUp",
    component: SignUpView,
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
