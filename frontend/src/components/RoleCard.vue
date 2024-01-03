<!-- RoleCard.vue -->
<template>
   {{ role.name }} at {{ role.company_name }}
</template>
  
  
<script>

export default {
  props: {
    role: {
      type: Object,
    },
  },
};
</script>
  
  