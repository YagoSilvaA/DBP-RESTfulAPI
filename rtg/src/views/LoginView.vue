<template>
  <div class="login">
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
        .post("http://localhost:5000/api/login", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          localStorage.setItem("token", response.data.token);
          this.$router.push("/");
        });
    },
  },
};
</script>

<style></style>
