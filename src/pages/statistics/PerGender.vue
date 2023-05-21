<template>
  <q-page padding class="column justify-center">
    <div class="text-center text-h2">Ops! Nada aqui...</div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, onMounted } from "vue";
import StatisticsService from "../../services/StatisticsService";
export default defineComponent({
  name: "PerGender",
  setup() {
    function getByGender() {
      StatisticsService.getByGender().then((response) => {
        console.log(response);
      });
    }
    onMounted(() => {
      getByGender();
    });
    return {};
  },
  components: {},
});
</script>

<style lang="scss" scoped></style>
