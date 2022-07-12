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
    <br /><button v-on:click="login1">log in</button>
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

<style>
.login h1 {
  font-size: 32px;
  font-weight: 300;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  text-transform: uppercase;
  margin-bottom: 24px;
}
.login input {
  width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin: 20px;
  margin-bottom: 0px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #2011ef;
  border-radius: 5px;
}
.login button {
  width: 200px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  background-color: #2011ef;
  color: #fff;
  border: none;
  border-radius: 5px;
}
</style>
<style>
.signup h1 {
  font-size: 32px;
  font-weight: 300;
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  text-transform: uppercase;
  margin-bottom: 24px;
}
.signup input {
  width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin: 20px;
  margin-bottom: 0px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #2011ef;
  border-radius: 5px;
}
.signup button {
  width: 200px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  background-color: #2011ef;
  color: #fff;
  border: none;
  border-radius: 5px;
}
</style>
