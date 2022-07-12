<template>
  <div class="signup">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/login">login</router-link> |
      <router-link to="/signup">Signup</router-link>
    </nav>
    <h1>Sign UP</h1>
    <input type="text" v-model="username" placeholder="Usuario" />
    <input type="password" v-model="password" placeholder="Password" />
    <br /><button v-on:click="signup1">Sign Up</button>
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
    signup1() {
      axios
        .post("http://127.0.0.1:5000/api/signup", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          localStorage.setItem("token", response.data.token);
          this.$router.push("/about");
        })
        .catch((error) => {
          this.mensaje_error = error.response.data.message;
          this.mostrar_mensaje = true;
        });
    },
  },
};
</script>

<style></style>
