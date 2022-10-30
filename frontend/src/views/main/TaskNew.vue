<template>
  <div class="mx-auto h-screen w-full sm:w-2/3 md:w-2/3">
    <form action="POST" @submit.prevent="createTask">
      <div class="bg-white rounded-xl w-full">
        <div class="space-y-4">
          <div>
            <label for="email" class="block mb-1 text-gray-600 font-medium"
              >Title</label
            >
            <input
              type="text" placeholder="Add the title here ..."
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
              v-model="task.title"
            />
          </div>
          <div>
            <label for="email" class="block mb-1 text-gray-600 font-medium"
              >Content</label
            >
            <textarea id="message" rows="4" v-model="task.content" class="block p-2.5 w-full text-sm   w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50" placeholder="Add you content here ..."></textarea>
          </div>
          
        </div>
        <button
          class="mt-4 w-full bg-teal-500 hover:bg-teal-700 focus:ring focus:ring-teal-100 text-white py-2 rounded-md text-lg tracking-wide"
        >
          Create Task
        </button>
                
        <div class="text-left" v-show="errorMessage" >
          <small class="text-red-600"
            >{{errorMessage}}</small
          >
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { CREATE_TASK } from "@/mutations";
import { useUserStore } from "@/stores/user";


export default {
  name: "TaskNew",

  components: {  },

  setup() {
    const userStore = useUserStore();
    return { userStore };
  },

  data() {
    return {
      task: { title: undefined, content: undefined},
      user: {
        isAuthenticated: false,
        token: this.userStore.getToken || "",
        info: this.userStore.getUser || {},
      },
      errorMessage: ""
    };
  },

  computed: {

  },

  async created() {
    if (this.user.token) {
      this.user.isAuthenticated = true;
    }
  },

  mounted() {

  },

  methods: {
    async createTask() {
      const task = await this.$apollo.mutate({
        mutation: CREATE_TASK,
        variables: {
          title: this.task.title,
          content: this.task.content, 
          isCompleted: false,
          userId: this.user.info.id
        },
      }).catch(err => {
        this.errorMessage = err
      });

      if(task){
        this.$router.push('/')
      }
    },
    toggleEdit() {
      this.showEdit = !this.showEdit;
    },

  },
};
</script>
