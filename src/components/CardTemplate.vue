<template>
  <q-card class="card">
    <div
      class="text-bold q-pl-md text-white text"
      :class="[
        { 'text-large': size == 'large' },
        { 'text-small': size == 'small' },
        { 'text-medium': size == 'medium' },
      ]"
    >
      {{ text }}
    </div>
    <q-img :src="image" class="image" fit="fill" />
  </q-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "CardTemplate",
  props: {
    size: {
      type: String,
      default: "medium",
    },
    text: {
      type: String,
      default: "Title Here",
    },
    image: {
      type: String,
    },
  },
  setup() {
    const random = Math.floor(Math.random() * 360); // Gera um valor aleatório entre 0 e 359
    return {};
  },
  components: {},
});
</script>

<style lang="scss" scoped>
.q-card {
  /* Estilos padrão do card */
  /* ... */
  position: relative;
  transform: scale(1); /* Define o tamanho normal do card */
  transition: transform 0.3s ease; /* Adiciona um efeito de transição suave */
  border: none; /* Remove a borda */
}

@media (max-width: $breakpoint-sm) {
  .q-card {
    height: 200px !important;
  }
}

.q-card:hover {
  /* Estilos quando o mouse está sobre o card */
  /* ... */
  transform: scale(1.08); /* Aumenta 5% o tamanho do card */
  border: 2px solid rgba(10, 6, 6, 0.626); /* Adiciona uma borda de 2px */
}
.text {
  text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black,
    1px 1px 0 black;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}
.text-small {
  padding-top: 8px;
  font-size: 20pt;
}
.text-medium {
  padding-top: 8px;
  font-size: 35pt;
}

.text-large {
  font-size: 50pt;
}
.image {
  height: 100%;
}
</style>
