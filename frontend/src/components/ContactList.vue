<template>
  <v-container>
    <v-toolbar :title="`Contacts (${contacts.length})`" color="secondary">
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
      <v-col v-for="contact in contacts" :key="contact.id" cols="12" md="6" lg="4">
        <contact-card :contact="contact" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ContactCard from './ContactCard.vue';

export default {
  components: {
    ContactCard,
  },
  data() {
    return {
      contacts: [],
      sortDirection: 'asc',
    };
  },
  mounted() {
    this.fetchContacts();
  },
  methods: {
    async fetchContacts() {
      const host = window.location.hostname;
      try {
        const response = await fetch(`http://${host}:8000/api/contacts`);
        const data = await response.json();
        this.contacts = data.results;
      } catch (error) {
        console.error('Error fetching contacts:', error);
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
      this.sortContacts();
    },
    sortJobs() {
      // Use slice to create a copy of the array and sort the copy
      const sortedContacts = this.contacts.slice().sort((a, b) => {
        // Sort by name
        const statusComparison = a.status.localeCompare(b.status);

        // If statuses are equal, then sort by title
        if (statusComparison === 0) {
          if (this.sortDirection === 'asc') {
            return a.lname.localeCompare(b.lname);
          } else {
            return b.lname.localeCompare(a.lname);
          }
        }

        // Otherwise, return the result of sorting by status
        return statusComparison;
      });

      // Update the original array with the sorted copy
      this.contacts.splice(0, this.jobs.length, ...sortedContacts);
    },
    addNewItem() {
      // Implement the logic to add a new item to your database
      window.location.href = "/admin/fcapi/contact/add/"
      //const newCompany = { id: this.companies.length + 1, name: 'New Company', /* other properties */ };
      //this.companies.push(newCompany);
      //this.filteredCompanies = [...this.companies]; // Update the filteredCompanies after adding a new item
      //console.log('Add new item logic here');
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
