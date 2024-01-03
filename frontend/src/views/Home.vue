<template>
  <v-container fluid>
    <!-- Header Component -->
    <Header @switch-view="switchView" :currentView="currentView" />

    <v-row>
      <!-- Main Content -->
      <v-col :cols="12">
        <!-- Main content goes here -->
        <v-card>
  
          <v-card-text>

            <!-- Include the JobList component -->
            <job-list v-if="currentView === 'jobs' || currentView === 'all'" />

            <!-- Include the CompanyList component -->
            <company-list v-if="currentView === 'companies' || currentView === 'all'" />

            <!-- Include the ContactList component -->
            <contact-list v-if="currentView === 'contacts' || currentView === 'all'" />

          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Footer Component -->
    <Footer />
  </v-container>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
import CompanyList from '@/components/CompanyList.vue';
import JobList from '@/components/JobList.vue';
import ContactList from '@/components/ContactList.vue';

export default {
  name: 'Home',
  components: {
    Header,
    Footer,
    CompanyList,
    JobList,
    ContactList,
  },
  data() {
    return {
      currentView: 'all', // Default view
    };
  },
  methods: {
    switchView(view) {
      this.currentView = view;
    },
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
