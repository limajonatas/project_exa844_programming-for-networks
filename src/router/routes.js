const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        name: "home",
        component: () => import("pages/IndexPage.vue"),
        meta: {
          title: "Home",
          subPage: true,
        },
      },
      {
        path: "/dados-gerais",
        name: "all-data",
        component: () => import("src/pages/statistics/AllStatistics.vue"),
        meta: {
          title: "Dados Gerais",
          subPage: true,
        },
      },
      {
        path: "/por-genero",
        name: "per-gender",
        component: () => import("src/pages/statistics/PerGender.vue"),
        meta: {
          title: "Por Gênero",
          subPage: true,
        },
      },
      {
        path: "/por-raca-cor",
        name: "per-race",
        component: () => import("src/pages/statistics/PerRace.vue"),
        meta: {
          title: "Por Raça/Cor",
          subPage: true,
        },
      },
      {
        path: "/por-grau-de-instrucao",
        name: "per-education",
        component: () => import("src/pages/statistics/PerEducation.vue"),
        meta: {
          title: "Por Grau de Instrução",
          subPage: true,
        },
      }
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
