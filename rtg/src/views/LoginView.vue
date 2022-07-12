<template>
  <div class="login">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/login">login</router-link> |
      <router-link to="/signup">Signup</router-link>
    </nav>
    <h1>Log In</h1>
    <input type="text" v-model="username" placeholder="Usuario" />
    <input type="password" v-model="password" placeholder="Password" />
    <button v-on:click="login1">log in</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login1() {
      axios
        .post("http://127.0.0.1:5000/api/login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          localStorage.setItem("token", response.data.token);
          localStorage.setItem("id", response.data.id);
          this.$router.push("/about");
        });
    },
  },
};
</script>

<style></style>
