<template>
  <v-card class="sm-card-height" @click="showJobDetails">
    <v-card-title>{{ job.title }}</v-card-title>
    <v-card-subtitle>{{ job.company.name }}</v-card-subtitle>
    <v-card-text class="trunc-3">{{ job.description }}</v-card-text>

    <!-- Displaying job details as colored chips -->
    <job-details-chips :job="job" />

    <v-card-actions>
      <v-btn v-if="job.url" text color="primary" @click="openLink(job.url)">
        Job description
      </v-btn>
      <v-btn v-else disabled text>
        No Job Description Available
      </v-btn>
    </v-card-actions>

    <!-- Include the JobDetailDialog component -->
    <job-detail-dialog :job="job" @close-dialog="closeDialog" ref="jobDetailDialog" />
  </v-card>
</template>

<script>
import JobDetailDialog from './JobDetailDialog.vue';
import JobDetailsChips from './JobDetailsChips.vue';

export default {
  props: {
    job: {
      type: Object,
    },
  },
  components: {
    JobDetailDialog,
    JobDetailsChips,
  },
 
  methods: {
    openLink(url) {
      if (url && url !== 'NA' && url !== 'Unknown') {
        // Open the link in a new tab
        window.open(url, '_blank');
      }
    },
    showJobDetails() {
      // Access the child component using $refs and update the dialog property
      if (this.$refs.jobDetailDialog) {
        this.$refs.jobDetailDialog.dialog = true;
      }
    },
    closeDialog() {
      // Access the child component using $refs and update the dialog property
      if (this.$refs.jobDetailDialog) {
        this.$refs.jobDetailDialog.dialog = false;
      }
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
