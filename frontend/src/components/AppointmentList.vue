<template>
  <div class="col-12 col-md-10 col-lg-7">
    <div class="list-group list-group-flush">
      <div v-for="apt in appointments" :key="apt">
        <!-- Delete appointment -->
        <button
          class="me-2 btn btn-sm btn-danger"
          @click="$emit('remove', apt.aptId, apt.id)"
          aria-label="Remove Appointment"
        >
          x
        </button>
        <div class="w-100">
          <div class="d-flex justify-content-between">
            <span
              class="h4 text-primary"
              contenteditable="contenteditable"
              @blur="
                $emit('edit', apt.aptId, 'petName', $event.target.innerText)
              "
            >
              {{ apt.petName }}
            </span>
            <span class="float-end">{{ formattedDate(apt.aptDate) }}</span>
          </div>
          <div class="owner-name">
            <span class="font-weight-bold text-primary me-1">Owner:</span>
            <span
              contenteditable="contenteditable"
              @blur="
                $emit('edit', apt.aptId, 'petOwner', $event.target.innerText)
              "
            >
              {{ apt.petOwner }}
            </span>
          </div>
          <div
            contenteditable="contenteditable"
            @blur="
              $emit('edit', apt.aptId, 'aptNotes', $event.target.innerText)
            "
          >
            {{ apt.aptNotes }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";

export default {
  name: "AppointmentList",
  props: ["appointments"],
  methods: {
    formattedDate: function (date) {
      moment.locale("es");
      return moment(new Date(date)).format("lll");
    },
  },
};
</script>
