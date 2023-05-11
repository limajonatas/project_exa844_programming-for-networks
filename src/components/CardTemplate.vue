<template>
  <q-card style="border: solid grey 1px" class="card">
    <div
      class="text-bold q-pl-md text-white text"
      :class="[
        { 'card-large': size == 'large' },
        { 'card-small': size == 'small' },
        { 'card-medium': size == 'medium' },
      ]"
      style="position: absolute; top: 0; left: 0; z-index: 1"
    >
      {{ text }}
    </div>
    <q-img
      :src="image"
      :class="[
        { 'image-large': size == 'large' },
        { 'image-small': size == 'small' },
        { 'image-medium': size == 'medium' },
      ]"
      fit="fill"
    />
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

<style lang="css" scoped>
.q-card:hover {
  transform: scale(1.08); /* Aumenta 5% o tamanho do card */
  transition: transform 0.3s ease; /* Adiciona um efeito de transição suave */
}
.q-card {
  position: relative;
}
.text {
  text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black,
    1px 1px 0 black;
}
.card-small {
  padding-top: 8px;
  font-size: 20pt;
}
.card-medium {
  padding-top: 8px;
  font-size: 35pt;
}

.card-large {
  font-size: 50pt;
}
.image-small {
  height: 138px;
  filter: blur(1.5px);
  filter: blur(1.5px) hue-rotate(90deg);
}
.image-medium {
  height: 240px;
  filter: blur(1.5px);
}
.image-large {
  height: 602px;
  filter: blur(1.5px) hue-rotate(180deg);
}
</style>
