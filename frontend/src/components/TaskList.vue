<template>
  <div class="h-100 w-full flex items-center justify-center bg-teal-lightest font-sans">
    <div class="bg-white rounded shadow p-6 m-4 w-full">
      <div class="mb-4">
        <div class="flex mt-4 items-right">
          <div class="w-full"></div>
          <button
            class="flex-no-shrink p-2 border-2 rounded text-teal border-teal hover:text-green-900 text-green-500 hover:bg-teal">
            <router-link :to="`/task/`">Add</router-link>
          </button>
        </div>
      </div>
      <div>
        <div class="flex mb-4 items-center" v-for="task in publishedTasks" :key="task.title">
          <router-link class="text-gray-900 w-full hover:text-blue-600" :to="`/task/${task.id}`">{{ task.title }}
          </router-link>
          <input id="default-checkbox" type="checkbox" value="" v-model="task.isCompleted"
            @change="toggleTaskComplete(task)"
            class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { UPDATE_TASK_COMPLETE } from "@/mutations";

  export default {
    name: "TaskListComponent",
    props: {
      tasks: {
        type: Array,
        required: true,
      },
    },
    computed: {
      publishedTasks() {
        return this.tasks.slice().reverse();
      },
    },
    methods: {
      async toggleTaskComplete(task) {
        const taskResp = await this.$apollo.mutate({
          mutation: UPDATE_TASK_COMPLETE,
          variables: {
            taskID: task.id,
            isCompleted: task.isCompleted,
          },
        });
        task.isCompleted = taskResp.data.updateTaskComplete.task.isCompleted;
      }
    },
  };
</script>