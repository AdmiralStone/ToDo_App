<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tasks</h1>
        <hr><br><br>
        <button type="button" v-b-modal.newTaskModal class="btn btn-success btn-sm">New Task</button>
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
           <tr v-for="task in taskArr.data" :key="task.SNo">
              <td >{{task.SNo}}</td>
              <td >{{task.Task}}</td>
              <td><span v-if="task.Status == 1">Completed</span>
                <span v-else>Pending</span></td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-success btn-sm" v-if="task.Status == 0" v-on:click="markCompleted(task)">Completed</button>
                  <button type="button" class="btn btn-danger btn-sm" v-on:click="deleteTask(task)">Delete</button> 
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- The modal -->
  <b-modal id="newTaskModal" ref="newTaskModal">
    <template>
      <p>Task</p>
      <input type="text" v-model="todoObj.Task">
    </template>
    

    <template v-slot:modal-footer="{ ok, cancel}">
      <!-- Emulate built in modal footer ok and cancel button actions -->
      <b-button size="sm" variant="success" @click="save()">
        OK
      </b-button>
      <b-button size="sm" variant="danger" @click="cancel()">
        Cancel
      </b-button>
    </template>
  </b-modal>

  </div>
</template>

<script>
import store from "@/store";
// import { mapState } from "vuex"

export default {
  data(){
    return{
      taskArr:[],
      todoObj:{"Task":null,"Status":0}
    };
  },
  methods:{
    getTods(){
      store.dispatch("todo/getTodoList").then(() => {
        this.taskArr = this.$store.state.todo.todoList
      })
      .catch(err => {
        console.log(err)
      })
    },

    markCompleted(taskObj){
      store.dispatch("todo/markTodoComplete",taskObj).then(()=>{
        this.taskArr = this.$store.state.todo.todoList
      })
      .catch(err => {
        console.log(err)
      })
    },

    deleteTask(taskObj){
      store.dispatch("todo/deleteTodo",taskObj).then(() =>{
        this.taskArr = this.$store.state.todo.todoList
      })
      .catch(err => {
        console.log(err)
      })
    },

    save(){
      store.dispatch("todo/createTodo",this.todoObj).then(() => {
        this.taskArr = this.$store.state.todo.todoList
        this.$refs['newTaskModal'].hide()
      })
      .catch(err =>{
        console.error(err)
      })
    }
  },
  created(){
    // var self = this;
    this.taskArr = 'TEST';
    this.getTods();
  }
};
</script>
