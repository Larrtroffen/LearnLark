import { createStore } from 'vuex';

export default createStore({
  state: {
    isAuthenticated: false,  // 用户是否已登录的状态
    userEmail: ''  // 用户邮箱
  },
  mutations: {
    login(state) {
      state.isAuthenticated = true;
    },
    logout(state) {
      state.isAuthenticated = false;
      state.userEmail = '';  // 注销时清除邮箱
    },
    setUserEmail(state, email: string) {
      state.userEmail = email;
    }
  },
  actions: {
    login({ commit }, email: string) {
      commit('login');
      commit('setUserEmail', email);  // 登录时设置邮箱
    },
    logout({ commit }) {
      commit('logout');
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    userEmail: (state) => state.userEmail,
  },
});