<template>
  <div class="home">
    <div class="flex flex-col place-items-center border-b-2">

      <h1 class="text-center text-5xl font-extrabold mb-5">
        {{ taskById.title }}
      </h1>
      <p class="text-gray-500 text-lg mb-2">
        {{ taskById.content }}
      </p>
    </div>

    <!-- Main content -->
    <div class="py-5 font-serif space-y-4">
      <div v-html="this.taskById.content"></div>
    </div>




  </div>
</template>

<script>
import { TASK_BY_ID } from "@/queries";
import { UPDATE_TASK_COMPLETE } from "@/mutations";


export default {
  name: "TaskView",

  components: {  },

  data() {
    return {
      taskById: null
    };
  },

  computed: {

  },

  async created() {
    // Get the task before the instance is mounted
    const task = await this.$apollo.query({
      query: TASK_BY_ID,
      variables: {
        id: this.$route.params.id,
      },
    });

    console.log(task.data.taskByI)
    this.taskById = task.data.taskById;

  },

  mounted() {

  },

  methods: {
    updateComplete() {
      this.isCompleted = !this.isCompleted;

      this.$apollo.mutate({
        mutation: UPDATE_TASK_COMPLETE,
        variables: {
          taskID: this.taskID,
        },
      });
    },
    toggleEdit() {
      this.showEdit = !this.showEdit;
    },

  },
};
</script>
