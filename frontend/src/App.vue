<template>
  <div class="container mx-auto max-w-3xl px-4 sm:px-6 xl:max-w-5xl xl:px-0">
    <div class="flex flex-col justify-between h-screen">
      <header class="flex flex-row items-center justify-between py-10">
        <div class="nav-logo text-2xl font-bold">
          <p>{{user.info.username}}</p>
        </div>
        <div class="nav-links hidden sm:block">
          <router-link
            to="/"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Home</router-link
          >
          <router-link
            v-if="!this.user.isAuthenticated"
            to="/signin"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Sign in</router-link
          >
          <router-link
            v-if="!this.user.isAuthenticated"
            to="/signup"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Sign up</router-link
          >
          <a
            v-if="this.user.isAuthenticated"
            @click="userSignOut()"
            class="mx-2 font-sans font-medium hover:underline hover:text-teal-700"
            >Sign Out</a
          >
        </div>
      </header>

      <router-view />

      <footer class="flex flex-col place-items-center mt-5 py-5 border-t-2">
        <div class="mb-3 flex space-x-4">
          
        </div>
        <div class="mb-3 flex space-x-1 text-sm text-gray-700">
          <div>
            Gaspare Scherma
          </div>
          <div>•</div>
          <div>© 2022</div>
          <div>•</div>
          <a href="/" class="hover:underline hover:text-teal-700"
            >Aidence interview assignment</a
          >
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const userStore = useUserStore();
    return { userStore };
  },

  data() {
    return {
      user: {
        isAuthenticated: false,
        token: this.userStore.getToken || "",
        info: this.userStore.getUser || {},
      },
    };
  },

  async created() {
    if (this.user.token) {
      this.user.isAuthenticated = true;
    }
  },
  
  methods: {
    userSignOut() {
      this.userStore.removeToken();
      this.userStore.removeUser();
      this.user.isAuthenticated = false

      window.location.href='/'

    },
  },
};
</script>
