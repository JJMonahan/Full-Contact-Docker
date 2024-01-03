<template>
    <v-col v-if="showSidebar" class="d-none d-lg-flex" cols="3">
     <v-card>
        <v-card-title>Navigation</v-card-title>
        <v-card-text>
          <v-list>
            <v-list-item v-for="(item, index) in sidebarItems" :key="index">
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-col>
  </template>
  
  <script>
  export default {
    props: {
      showSidebar: Boolean,
      sidebarItems: Array,
    },
  };
  </script>
  
  <style scoped>
  /* Add any custom styles here */
  </style>
  