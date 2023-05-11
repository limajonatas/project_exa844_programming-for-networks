<template>
  <q-page class="home">
    <card-template
      style="height: 100%"
      v-for="card in cards"
      :key="card.name"
      :size="card.size"
      :class="card.class"
      :text="card.title"
      :image="card.image"
      class="cursor-pointer"
      @click="navigateTo(card.name)"
    >
    </card-template>
  </q-page>
</template>

<script>
import { defineComponent, defineAsyncComponent } from "vue";
import { useQuasar } from "quasar";
import { useRoute } from "vue-router";
export default defineComponent({
  name: "IndexPage",
  setup() {
    const route = useRoute();
    const mobile = useQuasar();
    const cards = [
      {
        name: "all-data",
        size: mobile.platform.is.mobile ? "medium" : "large",
        class: "home__card-main",
        title: "Todos os Dados",
        image: "src/assets/images/all-data.jpg",
      },
      {
        name: "per-gender",
        size: mobile.platform.is.mobile ? "small" : "medium",
        class: "home__card-perGender",
        title: "Por Gênero",
        image: "src/assets/images/other.jpg",
      },
      {
        name: "per-education",
        size: "small",
        class: "home__card",
        title: "Por Grau de Instrução",
        image: "src/assets/images/other.jpg",
      },
      {
        name: "per-race",
        size: "small",
        class: "home__card",
        title: "Por Cor/Raça",
        image: "src/assets/images/other.jpg",
      },
    ];

    function navigateTo(name) {
      route.push({ name: name });
    }
    return {
      navigateTo,
      cards,
    };
  },
  components: {
    CardTemplate: defineAsyncComponent(() =>
      import("components/CardTemplate.vue")
    ),
  },
});
</script>
<style scoped lang="scss">
.home {
  display: flex;
  flex-direction: column;
  row-gap: 2rem;
  padding: 1rem;

  @media (min-width: $breakpoint-sm) {
    display: grid;
    grid-template-columns: repeat(2, auto);
    grid-template-rows: repeat(4, auto);
    padding: 4rem 11rem 4rem 11rem;
    gap: 2.5rem;

    &__card-main {
      grid-column: 1 / 2;
      grid-row: 1 / 5;
    }
    &__card-perGender {
      grid-column: 2 / 3;
      grid-row: 1 / 3;
    }
  }
}
</style>
