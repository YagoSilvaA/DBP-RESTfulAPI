<template>
  <div class="col-12 col-md-10 col-lg-7">
    <div class="input-group my-3">
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

      <ul class="dropdown-menu dropdown-menu-end">
        <li>
          <a
            href="#"
            class="dropdown-item d-flex justify-content-between align-items-center"
            id="petName"
            @click="$emit('requestKey', 'petName')"
          >
            Pet name
            <fa-icon icon="check" v-if="searchKey === 'petName'" />
          </a>
        </li>
        <li>
          <a
            href="#"
            class="dropdown-item d-flex justify-content-between align-items-center"
            id="aptDate"
            @click="$emit('requestKey', 'aptDate')"
          >
            Date
            <fa-icon icon="check" v-if="searchKey === 'aptDate'" />
          </a>
        </li>
        <li>
          <a
            href="#"
            class="dropdown-item d-flex justify-content-between align-items-center"
            id="petOwner"
            @click="$emit('requestKey', 'petOwner')"
          >
            Owner
            <fa-icon icon="check" v-if="searchKey === 'petOwner'" />
          </a>
        </li>
        <li><hr class="dropdown-divider" /></li>
        <li>
          <a
            href="#"
            class="dropdown-item d-flex justify-content-between align-items-center"
            id="asc"
            @click="$emit('requestDirection', 'asc')"
          >
            Asc
            <fa-icon icon="check" v-if="searchDirection === 'asc'" />
          </a>
        </li>
        <li>
          <a
            href="#"
            class="dropdown-item d-flex justify-content-between align-items-center"
            id="desc"
            @click="$emit('requestDirection', 'desc')"
          >
            Desc
            <fa-icon icon="check" v-if="searchDirection === 'desc'" />
          </a>
        </li>
      </ul>
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
