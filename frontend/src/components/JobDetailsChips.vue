<!-- JobDetailsChips.vue -->

<template>
    <div  class="pa-4">
    <v-chip :color="statusColor">{{ statusLabel }}</v-chip>
    <v-chip :color="priorityColor"> {{ priorityLabel }}</v-chip>
    <v-chip :color="locationColor"> {{ locationLabel }}</v-chip>
    <v-chip :color="compColor"> {{ compLabel }}</v-chip>
    <v-chip :color="travelColor"> {{ travelLabel }}</v-chip>
    <v-chip :color="qualColor"> {{ qualLabel }}</v-chip>
    </div>
  </template>
  
  <script>
  import { statusChoiceMappings, priorityChoiceMappings, locationChoiceMappings, travelChoiceMappings, compChoiceMappings, qualChoiceMappings } from '@/config/choiceMappings.js';
  
  export default {
    props: {
      job: {
        type: Object,
        required: true,
      },
    },
    computed: {
      statusColor() {
        return statusChoiceMappings[this.job.status]?.color || 'grey lighten-1';
      },
      statusLabel() {
        return statusChoiceMappings[this.job.status]?.label || this.job.status;
      },
      priorityColor() {
        return priorityChoiceMappings[this.job.priority]?.color || 'grey lighten-1';
      },
      priorityLabel() {
        return priorityChoiceMappings[this.job.priority]?.label || this.job.priority;
      },
      locationColor() {
        return locationChoiceMappings[this.job.location]?.color || 'grey lighten-1';
      },
      locationLabel() {
        return locationChoiceMappings[this.job.location]?.label || this.job.location;
      },
      travelColor() {
        return travelChoiceMappings[this.job.travel]?.color || 'grey lighten-1';
      },
      travelLabel() {
        return travelChoiceMappings[this.job.travel]?.label || this.job.travel;
      },
      compColor() {
        return compChoiceMappings[this.job.compensation]?.color || 'grey lighten-1';
      },
      compLabel() {
        return compChoiceMappings[this.job.compensation]?.label || this.job.compensation;
      },
      qualColor() {
        return qualChoiceMappings[this.job.qualifications]?.color || 'grey lighten-1';
      },
      qualLabel() {
        return qualChoiceMappings[this.job.qualifications]?.label || this.job.qualifications;
      },
    },
  };
  </script>
  