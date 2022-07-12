<template>
  <div class="col-12 col-md-10 col-lg-7">
    <div class="input-group my-3">
      <br />
      <input
        id="SearchApts"
        placeholder="Search"
        type="text"
        class="form-control"
        aria-label="Search Appointments"
        v-model="searchTerm"
      />

      <button
        type="button"
        class="btn btn-primary dropdown-toggle"
        data-bs-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        Sort by
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchAppointments",
  data() {
    return {
      searchTerm: "",
    };
  },
  watch: {
    searchTerm: function () {
      this.$emit("searchRecords", this.searchTerm);
    },
  },
  props: ["searchKey", "searchDirection"],
};
</script>
