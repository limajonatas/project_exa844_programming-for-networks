<template>
  <q-page class="home">
    <card-template
      :size="$q.platform.is.mobile ? 'md' : 'large'"
      class="home__card-large"
      text="Todos os Dados"
    >
    </card-template>
    <card-template
      :size="$q.platform.is.mobile ? 'small' : ''"
      class="home_card-second"
      text="Por Gênero"
    >
    </card-template>
    <card-template
      :size="$q.platform.is.mobile ? 'small' : ''"
      class="home_card-third"
      text="Por Cor/Raça"
    >
    </card-template>
    <card-template
      class="home_card-fourth"
      text="Por Escolaridade"
      :size="$q.platform.is.mobile ? 'small' : ''"
    >
    </card-template>
  </q-page>
</template>

<script>
import { defineComponent, defineAsyncComponent } from "vue";

export default defineComponent({
  name: "IndexPage",
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
    grid-template-rows: repeat(3, auto);
    padding: 2rem 8rem 2rem 8rem;
    gap: 2.5rem;

    &__card-large {
      grid-column: 1 / 2;
      grid-row: 1 / 4;
    }
    &__card-second {
      grid-column: 2 / 3;
      grid-row: 1 / 2;
    }
    &__card-third {
      grid-column: 2 / 3;
      grid-row: 2 / 3;
    }
    &__card-fourth {
      grid-column: 2 / 3;
      grid-row: 3 / 4;
    }
  }
}
</style>
