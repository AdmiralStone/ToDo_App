<template>
  <div class="home">
   <!-- Here a list of tasks will be displayed with 2 action buttons -->
    <table>
      <tr>
        <th>Task Number</th>
        <th>Task</th>
        <th>Status</th>
      </tr>
      <tr v-for="task in msg" :key="task.No">
        <td >{{task.No}}</td>
        <td >{{task.Task}}</td>
        <td>{{task.Status}}</td>
      </tr>
    </table>

  </div>
</template>

<script>
import store from "@/store";
// import { mapState } from "vuex"

export default {
  data(){
    return{
      msg:null
    };
  },
  methods:{
    getTods(){
      store.dispatch("todo/getTodoList").then(() => {
        this.msg = this.$store.state.todo.todoList
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  created(){
    // var self = this;
    this.msg = 'TEST';
    this.getTods();
  }
};
</script>
