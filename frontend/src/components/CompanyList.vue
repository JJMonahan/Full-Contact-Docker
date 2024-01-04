<template>
  <v-container>
    <v-toolbar :title="`Companies (${filteredCompanies.length})`" color="secondary">
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
      <v-col v-for="company in filteredCompanies" :key="company.id" cols="12" md="6" lg="4">
        <!-- Use the CompanyCard component and pass the company data as a prop -->
        <company-card :company="company" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import CompanyCard from './CompanyCard.vue';

export default {
  components: {
    CompanyCard,
  },
  data() {
    return {
      companies: [],
      filteredCompanies: [],
      sortDirection: 'asc',
    };
  },
  mounted() {
    this.fetchCompaniesData();
  },
  methods: {
    async fetchCompaniesData() {
      try {
        const host = window.location.hostname;
        const response = await this.$axios.get('http://${host}:8000/api/companies/');
        this.companies = response.data.results;
        this.filteredCompanies = [...this.companies]; // Initialize filteredCompanies with all companies
      } catch (error) {
        console.error('Error fetching data:', error);
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
      this.sortCompanies();
    },
    sortCompanies() {
      // Use the JavaScript sort method on the filteredCompanies array
      this.filteredCompanies.sort((a, b) => {
        if (this.sortDirection === 'asc') {
          return a.name.localeCompare(b.name);
        } else {
          return b.name.localeCompare(a.name);
        }
      });
    },
    addNewItem() {
      // Implement the logic to add a new item to your database
      window.location.href = "/admin/fcapi/company/add/"
      //const newCompany = { id: this.companies.length + 1, name: 'New Company', /* other properties */ };
      //this.companies.push(newCompany);
      //this.filteredCompanies = [...this.companies]; // Update the filteredCompanies after adding a new item
      //console.log('Add new item logic here');
    },
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
