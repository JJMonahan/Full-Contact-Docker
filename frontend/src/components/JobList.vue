<template>
  <v-container>
    <v-toolbar :title="`Jobs (${jobs.length})`" color="secondary">
      <v-spacer></v-spacer>
      <!-- Filter button with icon -->
      <v-btn icon @click="openFilterDialog">
        <v-icon>mdi-filter</v-icon>
      </v-btn>

      <!-- Sort button with icon -->
      <v-btn icon @click="toggleSortDirection">
        <v-icon>{{ sortDirection === 'asc' ? 'mdi-sort-ascending' : 'mdi-sort-descending' }}</v-icon>
      </v-btn>

      <!-- The button with a plus sign for adding a new item -->
      <v-btn @click="addNewItem" icon>
        <v-icon>mdi-plus</v-icon>
      </v-btn>
    </v-toolbar>
    <v-row>
      <v-col v-for="job in jobs" :key="job.id" cols="12" md="6" lg="4">
        <!-- Use the JobCard component and pass the job data as a prop -->
        <job-card :job="job" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import JobCard from './JobCard.vue';

export default {
  components: {
    JobCard,
  },
  data() {
    return {
      jobs: [],
      sortDirection: 'asc',
    };
  },
  mounted() {
    this.fetchJobs();
  },
  methods: {
    async fetchJobs() {
      try {
        const response = await fetch('http://localhost:8000/api/jobs');
        const data = await response.json();
        this.jobs = data.results;
      } catch (error) {
        console.error('Error fetching jobs:', error);
      }
    },
    openLink(url) {
      if (url && url !== 'NA' && url !== 'Unknown') {
        // Open the link in a new tab
        window.open(url, '_blank');
      }
    },
    openFilterDialog() {
      // Implement the logic to open the filter dialog
      console.log('Open filter dialog logic here');
    },
    toggleSortDirection() {
      // Implement the logic to toggle the sort direction
      this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
      console.log('Toggle sort direction logic here');
      this.sortJobs();
    },
    sortJobs() {
      // Use slice to create a copy of the array and sort the copy
      const sortedJobs = this.jobs.slice().sort((a, b) => {
        // First, sort by status
        const statusComparison = a.status.localeCompare(b.status);

        // If statuses are equal, then sort by title
        if (statusComparison === 0) {
          if (this.sortDirection === 'asc') {
            return a.title.localeCompare(b.title);
          } else {
            return b.title.localeCompare(a.title);
          }
        }

        // Otherwise, return the result of sorting by status
        return statusComparison;
      });

      // Update the original array with the sorted copy
      this.jobs.splice(0, this.jobs.length, ...sortedJobs);
    },
    addNewItem() {
      // Implement the logic to add a new item to your database
      console.log('Add new item logic here');
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
