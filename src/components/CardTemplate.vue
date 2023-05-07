<template>
  <q-card>
    <q-card-section :class="size == 'large' ? 'q-px-xl' : 'q-pa-sm'">
      <div
        v-if="size == 'large'"
        class="text-bold q-py-none"
        style="font-size: 50pt"
      >
        {{ text }}
      </div>
      <div
        v-else-if="size == 'small'"
        class="text-bold q-py-none"
        style="font-size: 20pt"
      >
        {{ text }}
      </div>
      <div v-else class="text-bold q-py-none" style="font-size: 30pt">
        {{ text }}
      </div>
    </q-card-section>
  </q-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "CardTemplate",
  props: {
    size: {
      type: String,
      required: false,
    },
    text: {
      type: String,
      required: false,
    },
  },
  setup() {
    return {};
  },
  components: {},
});
</script>

<style lang="css" scoped>
.q-card:hover {
  transform: scale(1.1); /* Aumenta 5% o tamanho do card */
  transition: transform 0.3s ease; /* Adiciona um efeito de transição suave */
}
</style>
