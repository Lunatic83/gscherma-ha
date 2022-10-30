<template>
  <div class="mx-auto h-screen w-full sm:w-2/3 md:w-2/3">
    <form action="POST" @submit.prevent="createUpdateTask">
      <div class="bg-white rounded-xl w-full">
        <div class="space-y-4">
          <div>
            <label for="title" class="block mb-1 text-gray-600  w-full font-medium">Title:</label>
            <label v-if="!showEdit" for="title" class="block mb-1 text-black-600 font-medium">{{task.title}}</label>

            <input v-if="showEdit" type="text" placeholder="Add the title here ..."
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
              v-model="task.title" />
          </div>
          <div>
            <label for="content" class="block mb-1 text-gray-600 font-medium">Content:</label>
            <label v-if="!showEdit" for="title" class="block mb-1 text-black-600 font-medium">{{task.content}}</label>

            <textarea v-if="showEdit"  id="message" rows="4" v-model="task.content"
              class="block p-2.5 w-full text-sm w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
              placeholder="Add you content here ..."></textarea>
          </div>
          <div>
            <!-- <label for="completed" class="block mb-1 w-full text-gray-600 font-medium">Completed
            <input id="default-checkbox" type="checkbox" value="" v-model="task.isCompleted" :disabled="showEdit"
              class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
            </label> -->
            <div class="flex items-center mb-4">
              <input :disabled="!showEdit" id="disabled-checkbox" type="checkbox" v-model="task.isCompleted" class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
              <label for="disabled-checkbox" class="ml-2 text-sm font-medium text-gray-400 dark:text-gray-500">Completed</label>
          </div>
          </div>
        </div>

        <button v-if="showEdit" 
          class="mt-4 w-full bg-teal-500 hover:bg-teal-700 focus:ring focus:ring-teal-100 text-white py-2 rounded-md text-lg tracking-wide">
          {{ $route.params.id ? "Update Task" : "Create Task" }}
        </button>
        <button v-if="!showEdit" @click="toggleEdit"
          class="mt-4 w-full bg-teal-500 hover:bg-teal-700 focus:ring focus:ring-teal-100 text-white py-2 rounded-md text-lg tracking-wide">
          Edit
        </button>

        <div class="text-left" v-show="errorMessage">
          <small class="text-red-600">{{ errorMessage }}</small>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
  import { CREATE_TASK, UPDATE_TASK } from "@/mutations";
  import { useUserStore } from "@/stores/user";
  import { TASK_BY_ID } from "@/queries";

  export default {
    name: "TaskNew",

    components: {},

    setup() {
      const userStore = useUserStore();
      return { userStore };
    },

    data() {
      return {
        showEdit: false, 
        task: { title: undefined, content: undefined, isCompleted: false },
        user: {
          isAuthenticated: false,
          token: this.userStore.getToken || "",
          info: this.userStore.getUser || {},
        },
        errorMessage: "",
      };
    },

    computed: {},

    async created() {
      if (this.user.token) {
        this.user.isAuthenticated = true;
      }

      if (this.$route.params.id) {
        this.showEdit = false
        // Get the task before the instance is mounted
        let task = await this.$apollo.query({
          query: TASK_BY_ID,
          variables: {
            id: this.$route.params.id,
          },
        });
        this.task = Object.assign({}, task.data.taskById);
      }else {
        this.showEdit = true
      }
    },

    mounted() { },

    methods: {
      async createUpdateTask() {
        let task = undefined;
        if (this.$route.params.id) {
          task = await this.$apollo
            .mutate({
              mutation: UPDATE_TASK,
              variables: {
                taskId: this.task.id,
                title: this.task.title,
                content: this.task.content,
                isCompleted: this.task.isCompleted,
              },
            })
            .catch((err) => {
              this.errorMessage = err;
            });
        } else {
          task = await this.$apollo
            .mutate({
              mutation: CREATE_TASK,
              variables: {
                title: this.task.title,
                content: this.task.content,
                isCompleted: false,
              },
            })
            .catch((err) => {
              this.errorMessage = err;
            });
        }

        if (task) {
            this.$router.push("/");
        }
      },

      toggleEdit() {
        this.showEdit = !this.showEdit;
      },
    },
  };
</script>