import Vue from "vue";
import Vuex from "vuex";
import * as todo from "./modules/todo.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    todo
  }
});
