const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("pages/IndexPage.vue"),
        meta: {
          title: "Home",
          subPage: false,
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
