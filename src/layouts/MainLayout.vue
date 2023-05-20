<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="row">
        <q-btn-group push>
          <q-btn
            v-for="link in linksList"
            :key="link.name"
            flat
            :label="$route.name == link.name ? $route.meta.title : ''"
            :icon="link.icon"
            @click="$router.push({ name: link.name })"
            :class="{ 'bg-cyan': $route.name == link.name }"
          >
            <q-tooltip v-if="!($route.name == link.name)">
              {{ link.title }}
            </q-tooltip>
          </q-btn>
        </q-btn-group>

        <q-toolbar-title class="text-right text-bold text-white text-h6">
          Estatísticas Eleições Brasileira
        </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref, computed } from "vue";
import { useRoute } from "vue-router";

export default defineComponent({
  name: "MainLayout",

  setup() {
    const showTitle = ref(false);
    const route = useRoute();
    const linksList = computed(() => {
      let data = [
        {
          title: "Home",
          name: "home",
          icon: "home",
        },
        {
          title: "Dados Gerais",
          name: "all-data",
          icon: "assessment",
        },
        {
          title: "Por Gênero",
          name: "per-race",
          icon: "people",
        },
        {
          title: "Por Grau de Instrução",
          name: "per-education",
          icon: "school",
        },
      ];

      return data;
    });

    return {
      showTitle,
      linksList,
    };
  },
});
</script>

<style></style>
