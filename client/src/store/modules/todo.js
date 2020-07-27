import EventService from '@/services/EventService.js';

export const namespaced = true;

export const state = {
    todoList : null
}

export const mutations ={
    SET_TODO(state,todos){
        state.todoList = todos
    }
}

export const actions = {
    getTodoList({commit}){
        console.log("Reached Here")
        return EventService.getToDoList().then(res => {
            let todos = res.data
            commit('SET_TODO' , todos)
        })
        .catch(error => {
            throw error
        })
    }
}