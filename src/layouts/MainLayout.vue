<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="row">
        <q-btn-group push v-if="$q.platform.is.desktop">
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

        <q-btn v-else color="white" icon="menu" flat class="q-pl-none q-pr-xs">
          <q-menu>
            <q-list>
              <q-item
                v-for="link in linksList"
                :key="link.name"
                clickable
                v-close-popup
                @click="$router.push({ name: link.name })"
                :class="{ 'bg-cyan': $route.name == link.name }"
              >
                <q-item-section>
                  <q-item-label>
                    {{ link.title }}
                  </q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>

        <q-toggle v-model="dark" color="secondary" :icon="dark ? 'nightlight':'light_mode'" :size="$q.platform.is.desktop ? 'lg':'md'"/>

        <q-toolbar-title
          class="text-right text-bold text-white"
          :class="$q.platform.is.desktop ? 'text-h6' : 'text-subtitle1'"
        >
          <q-img
            src="icons/favicon-96x96.png"
            class="q-pa-sm"
            :style="$q.platform.is.desktop ? 'height: 40px; width: 40px':'height: 20px; width: 20px'"
          />
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
import { Dark } from "quasar";
import { defineComponent, ref, computed, watch } from "vue";
import { useRoute } from "vue-router";

export default defineComponent({
  name: "MainLayout",

  setup() {
    const showTitle = ref(false);
    const linksList = computed(() => {
      let data = [
        {
          title: "Página Inicial",
          name: "home",
          icon: "home",
        },
        {
          title: "Por Gênero",
          name: "per-gender",
          icon: "male",
        },
        {
          title: "Por Cor/Raça",
          name: "per-race",
          icon: "groups",
        },
        {
          title: "Por Grau de Instrução",
          name: "per-education",
          icon: "school",
        },
      ];

      return data;
    });
    const dark = ref(false);
    watch(
      () => dark.value,
      () => {
        Dark.toggle();
      }
    );
    return {
      showTitle,
      linksList,
      dark
    };
  },
});
</script>

<style></style>
