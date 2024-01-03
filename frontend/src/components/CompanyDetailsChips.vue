<!-- JobDetailsChips.vue -->

<template>
    <div  class="pa-4">
    <v-chip :color="categoryColor">{{ categoryLabel }}</v-chip>
    <v-chip :color="realmColor"> {{ realmLabel }}</v-chip>
    <v-chip :color="sizeColor"> {{ sizeLabel }}</v-chip>
    <v-chip :color="priorityColor"> {{ priorityLabel }}</v-chip>
    </div>
  </template>
  
  <script>
  import { categoryChoiceMappings, priorityChoiceMappings, realmChoiceMappings, sizeChoiceMappings } from '@/config/choiceMappings.js';
  
  export default {
    props: {
      company: {
        type: Object,
        required: true,
      },
    },
    computed: {
      realmColor() {
        return realmChoiceMappings[this.company.realm]?.color || 'grey lighten-1';
      },
      realmLabel() {
        return realmChoiceMappings[this.company.realm]?.label || this.realm.status;
      },
      priorityColor() {
        return priorityChoiceMappings[this.company.priority]?.color || 'grey lighten-1';
      },
      priorityLabel() {
        return priorityChoiceMappings[this.company.priority]?.label || this.job.priority;
      },
      sizeColor() {
        return sizeChoiceMappings[this.company.size]?.color || 'grey lighten-1';
      },
      sizeLabel() {
        return sizeChoiceMappings[this.company.size]?.label || this.company.size;
      },
      categoryColor() {
        return categoryChoiceMappings[this.company.category]?.color || 'grey lighten-1';
      },
      categoryLabel() {
        return categoryChoiceMappings[this.company.category]?.label || this.company.category;
      },
  
    },
  };
  </script>
  