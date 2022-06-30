<template>
  <div id="main-app" class="container mt-3">
    <h1 class="fw-bold"><span class="vue-js">Vue.js</span> Pet Appointments</h1>
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

import AppointmentList from "./components/AppointmentList";
import AddAppointment from "./components/AddAppointment.vue";
import SearchAppointments from "./components/SearchAppointments.vue";

export default {
  name: "MainApp",
  data: function () {
    return {
      appointments: [],
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
    axios.get("./data/appointments.json").then(
      (response) =>
        (this.appointments = response.data.map((item) => {
          item.aptId = this.aptIndex;
          this.aptIndex++;
          return item;
        }))
    );
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
    removeItem: function (apt) {
      this.appointments = _.without(this.appointments, apt);
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
  color: #42b983;
}
</style>
