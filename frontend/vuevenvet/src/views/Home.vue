<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <navigation/>
    <h1>Home</h1>
    <p v-if="userLogged">User loggued: {{userLogged}}</p>
  </div>
  
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {
    Navigation
    
  },
};
</script>
