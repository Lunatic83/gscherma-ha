<template>
  <div class="home">
    <h1 class="text-5xl font-extrabold mb-2">A Task manager for Aidence</h1>
    <p class="text-gray-500 text-lg mb-5">
      Task List
    </p>
    <task-list v-if="user.isAuthenticated" :tasks="this.allTasks"></task-list>
    <div v-if="!user.isAuthenticated">
      Sign in to show yout tasks
    </div>
  </div>
</template>

<script>
  // @ is an alias to /src
  import TaskList from "@/components/TaskList.vue";
  import { ALL_TASKS } from "@/queries";
  import { useUserStore } from "@/stores/user";

  export default {
    components: { TaskList },
    name: "HomeView",

    setup() {
      const userStore = useUserStore();
      return { userStore };
    },

    data() {
      return {
        allTasks: [],
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

      if(this.user.isAuthenticated){
        const tasks = await this.$apollo.query({
          query: ALL_TASKS,
        });
        this.allTasks = tasks.data.allTasks;
      }

    },
  };
</script>