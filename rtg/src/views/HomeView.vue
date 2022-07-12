<template>
  <div class="home">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/login">login</router-link> |
      <router-link to="/signup">Signup</router-link>
    </nav>
    <HelloWorld msg="Welcome to VenVet" />
    <center><img alt="Vue logo" src="../assets/logo.png" width="300" /></center>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "HomeView",
  components: {
    HelloWorld,
  },
};
</script>
