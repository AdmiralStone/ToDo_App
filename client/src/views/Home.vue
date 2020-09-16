<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">New Task</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">S.No</th>
              <th scope="col">Task</th>
              <th scope="col">Status</th>
              <th scope="col">Action</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
           <tr v-for="task in msg.data" :key="task.taskId">
              <td >{{task.taskId}}</td>
              <td >{{task.Task}}</td>
              <td>{{task.Status}}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-success btn-sm" v-if="task.Status == 0" v-on:click="markCompleted(task)">Completed</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button> 
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
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
    },

    markCompleted(taskObj){
      store.dispatch("todo/markTodoComplete",taskObj).then(()=>{
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
