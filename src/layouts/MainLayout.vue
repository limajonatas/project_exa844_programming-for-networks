<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="row">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
          v-if="$route.meta.subPage"
        />
        <q-toolbar-title class="text-right">
          {{ $route.meta.title }}
        </q-toolbar-title>
        <q-toolbar-title class="text-right text-bold text-black text-h5">
          Estatísticas Eleições Brasileira
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" v-if="$route.meta.subPage" bordered>
      <q-list>
        <q-item-label header> Menu </q-item-label>

        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref, computed } from "vue";
import EssentialLink from "components/EssentialLink.vue";
import { useRoute } from "vue-router";

export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);
    const route = useRoute();
    const linksList = computed(() => {
      let data = [
        {
          title: "Dados Gerais",
          icon: "home",
          link: "",
        },
        {
          title: "Por Gênero",
          icon: "people",
          link: "",
        },
        {
          title: "Por Grau de Instrução",
          icon: "school",
          link: "",
        },
        {
          title: "Por Cor/Raça",
          icon: "groups",
          link: "",
        },
      ];

      if (route.name == "all-data")
        data = data.filter((item) => item.title != "Dados Gerais");
      else if (route.name == "per-gender")
        data = data.filter((item) => item.title != "Por Gênero");
      else if (route.name == "per-education")
        data = data.filter((item) => item.title != "Por Grau de Instrução");
      else if (route.name == "per-race")
        data = data.filter((item) => item.title != "Por Cor/Raça");

      return data;
    });
    return {
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      linksList,
    };
  },
});
</script>
