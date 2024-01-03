<template>
  <v-app-bar app>
    <v-toolbar-title>Full Contact</v-toolbar-title>
    <v-btn
      text
      @click="switchView(item.view)"
      v-for="(item, index) in headerLinks"
      :key="index"
      :class="{ 'active-link': currentView === item.view }"
    >
      {{ item.title }}
    </v-btn>
    <hr>
  </v-app-bar>
</template>

<script>
export default {
  props: ['currentView'],
  computed: {
    headerLinks() {
      return [
        { title: 'All Sections', icon: 'mdi-briefcase-outline', view: 'all' },
        { title: 'Companies', icon: 'mdi-briefcase-outline', view: 'companies' },
        { title: 'Jobs', icon: 'mdi-briefcase', view: 'jobs' },
        { title: 'Dashboard', icon: 'mdi-view-dashboard', view: 'dashboard' },
        { title: 'Profile', icon: 'mdi-account', view: 'profile' },
        { title: 'Settings', icon: 'mdi-cog', view: 'settings' },
      ];
    },
  },
  methods: {
    switchView(view) {
      this.$emit('switch-view', view);
    },
  },
};
</script>

<style scoped>
.active-link {
  color: darkblue; /* You can adjust the color as needed */
}
</style>
