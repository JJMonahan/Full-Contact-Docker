<!-- ContactCard.vue -->

<template>
  <v-card class="sm-card-height" @click="showContactDetails">
    <v-card-title>{{ contact.fname }} {{ contact.lname }}</v-card-title>

    <div class="pl-4 pr-4" v-for="role in contact.role" :key="role.id">
      <role-card :role="role" />
    </div>

    <!-- Email Link -->
    <div class="pl-4 pr-4 pt-4">
      <a :href="'mailto:' + contact.email">{{ contact.email }}</a>
    </div>

    <!-- URL Link -->
    <div class="pl-4 pr-4">
      <a :href="contact.url" target="_blank">{{ contact.url }}</a>
    </div>

    <!-- Phone Link -->
    <div class="pl-4 pr-4">
      <a :href="'tel:' + contact.phone">{{ contact.phone }}</a>
    </div>
  </v-card>

  <!-- Include the contactDetailDialog component -->
  <contact-detail-dialog :contact="contact" @close-dialog="closeDialog" ref="contactDetailDialog" />

</template>

<script>
import RoleCard from "./RoleCard.vue";
import ContactDetailDialog from "./ContactDetailDialog.vue";

export default {
  props: {
    contact: {
      type: Object,
    },
  },
  components: {
    ContactDetailDialog,
    RoleCard,
  },
  methods: {

    showContactDetails() {
      if (this.$refs.contactDetailDialog) {
        this.$refs.contactDetailDialog.dialog = true;
      }
     
    },
    closeDialog() {
      // Access the child component using $refs and update the dialog property
      if (this.$refs.contactDetailDialog) {
        this.$refs.contactDetailDialog.dialog = false;
      }
    },
    openEmailLink(email) {
      if (email && email !== 'NA' && email !== 'Unknown') {
        // Open the link in a new tab
        window.open('mailto:' + email, '_blank');
      }
    },
    openUrlLink(url) {
      if (url && url !== 'NA' && url !== 'Unknown') {
        // Open the link in a new tab
        window.open(url, '_blank');
      }
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>