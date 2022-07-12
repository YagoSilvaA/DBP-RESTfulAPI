<template>
  <div id="main-app" class="container mt-3">
    <button @click="logOut">Log out</button>
    <h1 class="fw-bold"><span class="vue-js">VenVet</span> Pet Appointments</h1>
    <div class="row justify-content-center">
      <add-appointment @add="addItem" />
      <search-appointments
        :searchKey="filterKey"
        :searchDirection="filterDirection"
        @searchRecords="searchAppointments"
        @requestKey="changeKey"
        @requestDirection="changeDirection"
      />
      <appointment-list
        :appointments="filteredApts"
        @remove="removeItem"
        @edit="editItem"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

import AppointmentList from "../components/AppointmentList.vue";
import AddAppointment from "../components/AddAppointment.vue";
import SearchAppointments from "../components/SearchAppointments.vue";

export default {
  name: "AboutView",
  data: function () {
    return {
      appointments: [],
      apo: [],
      aptIndex: 0,
      searchTerms: "",
      filterKey: "petName",
      filterDirection: "asc",
    };
  },
  components: {
    AppointmentList,
    AddAppointment,
    SearchAppointments,
  },
  mounted() {
    let vue = this;
    axios.get("http://127.0.0.1:5000/api/citas1").then(function (response) {
      vue.apo = response.data.citas;
      console.log(vue.posts);
    });

    axios.get("http://127.0.0.1:5000/api/citas1").then(
      (response) =>
        (this.appointments = response.data.citas.map((item) => {
          item.aptId = this.aptIndex;
          this.aptIndex++;
          return item;
        }))
    );

    let user = localStorage.getItem("token");
    if (!user) {
      this.$router.push("/signup");
    }
  },
  computed: {
    searchedApts: function () {
      return this.appointments.filter((item) => {
        return (
          item.petName.toLowerCase().match(this.searchTerms.toLowerCase()) ||
          item.petOwner.toLowerCase().match(this.searchTerms.toLowerCase()) ||
          item.aptNotes.toLowerCase().match(this.searchTerms.toLowerCase())
        );
      });
    },
    filteredApts: function () {
      return _.orderBy(
        this.searchedApts,
        (item) => {
          return item[this.filterKey].toLowerCase();
        },
        this.filterDirection
      );
    },
  },
  methods: {
    logOut() {
      axios
        .post("http://127.0.0.1:5000/api/logout", null, {
          headers: {
            "Content-Type": "application/json",
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
        })
        .then(() => {
          localStorage.removeItem("token");
          localStorage.removeItem("id");
          this.$router.push("/");
        })
        .catch((error) => {
          this.fail.mensaje = error.response.data.message;
          this.fail.show = true;
        });
    },
    removeItem: function (apt, id) {
      axios.post("http://127.0.0.1:5000/api/citas12", {
        id: id,
      });

      this.appointments = _.without(this.appointments, apt);

      let vue = this;
      axios.get("http://127.0.0.1:5000/api/citas1").then(function (response) {
        vue.appointments = response.data.citas;
        console.log(vue.posts);
      });
    },
    editItem: function (id, field, text) {
      const aptIndex = _.findIndex(this.appointments, {
        aptId: id,
      });
      this.appointments[aptIndex][field] = text;
    },
    addItem: function (apt) {
      apt.aptId = this.aptIndex;
      this.aptIndex++;
      this.appointments.push(apt);
    },
    searchAppointments: function (terms) {
      this.searchTerms = terms;
    },
    changeKey: function (key) {
      this.filterKey = key;
    },
    changeDirection: function (direction) {
      this.filterDirection = direction;
    },
  },
};
</script>

<style scoped>
.container {
  min-width: 340px;
}
.vue-js {
  color: #424cb9;
}
</style>
