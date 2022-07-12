<template>
  <div class="col-11">
    <div class="card my-4">
      <div
        class="card-header bg-primary text-white"
        :class="{ 'rounded-bottom': hidepanel }"
        @click="hidepanel = !hidepanel"
        tabindex="0"
        role="button"
        :aria-pressed="hidepanel ? 'false' : 'true'"
      >
        <fa-icon icon="plus" class="me-3" />
        <button><b>Add Appointment</b></button>
        <br />
      </div>

      <transition>
        <div v-if="!hidepanel" class="card-body">
          <form id="aptForm" @submit.prevent="requestAdd">
            <div class="row mb-3">
              <label for="petName" class="col-md-2 col-form-label text-md-end">
                Pet Name
              </label>
              <div class="col-md-10">
                <input
                  type="text"
                  name="petName"
                  id="petName"
                  class="form-control"
                  placeholder="Pet's Name"
                  aria-label="Pet's Name"
                  v-model="formData.petName"
                />
              </div>
            </div>

            <div class="row mb-3">
              <label for="petOwner" class="col-md-2 col-form-label text-md-end">
                Pet Owner
              </label>
              <div class="col-md-10">
                <input
                  type="text"
                  name="petOwner"
                  id="petOwner"
                  class="form-control"
                  placeholder="Owner's Name"
                  v-model="formData.petOwner"
                />
              </div>
            </div>

            <div class="row mb-3">
              <label for="aptDate" class="col-md-2 col-form-label text-md-end">
                Date
              </label>
              <div class="col-md-4">
                <input
                  type="date"
                  name="aptDate"
                  id="aptDate"
                  class="form-control"
                  v-model="formData.aptDate"
                />
              </div>
              <label for="aptTime" class="col-md-2 col-form-label text-md-end">
                Time
              </label>
              <div class="col-md-4">
                <input
                  type="time"
                  name="aptTime"
                  id="aptTime"
                  class="form-control"
                  v-model="formData.aptTime"
                />
              </div>
            </div>

            <div class="row mb-3">
              <label for="aptNotes" class="col-md-2 col-form-label text-md-end">
                Apt. Notes
              </label>
              <div class="col-md-10">
                <textarea
                  name="aptNotes"
                  id="aptNotes"
                  rows="4"
                  class="form-control"
                  placeholder="Appointment Notes"
                  v-model="formData.aptNotes"
                >
                </textarea>
              </div>
            </div>

            <div class="row mb-3">
              <div class="col-md-10 offset-md-2">
                <button
                  type="submit"
                  class="btn btn-primary d-block ms-auto"
                  v-on:click="citas"
                >
                  Add Appointment
                </button>
              </div>
            </div>
          </form>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "AddAppointment",
  data() {
    return {
      formData: [],
      hidepanel: true,
    };
  },
  methods: {
    citas() {
      axios.post("http://127.0.0.1:5000/api/citas", {
        petName: this.formData.petName,
        petOwner: this.formData.petOwner,
        aptDate: this.formData.aptDate + " " + this.formData.aptTime,
        aptNotes: this.formData.aptNotes,
        id: localStorage.getItem("id"),
      });
    },

    requestAdd: function () {
      this.formData = {
        petName: this.formData.petName,
        petOwner: this.formData.petOwner,
        aptDate: this.formData.aptDate + " " + this.formData.aptTime,
        aptNotes: this.formData.aptNotes,
      };
      this.$emit("add", this.formData);
      this.formData = [];
      this.hidepanel = true;
    },
  },
};
</script>

<style scoped>
.card-header {
  cursor: pointer;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.7s ease-in-out;
}

.v-enter,
.v-leave-to {
  opacity: 0;
}
</style>
