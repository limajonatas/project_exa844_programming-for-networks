<template>
  <q-page padding class="per-race-page q-gutter-y-md">
    <q-card class="q-pa-md per-race-page__candidates">
      <q-card-section>
        <h1
          :class="
            $q.platform.is.desktop ? 'text-h6' : 'text-subtitle1 text-center'
          "
        >
          CANDIDATOS POR RAÇA
        </h1>

        <div class="row justify-center">
          <div class="col-12">
            <bar-chart
              :series="candidatesSeries"
              :categories="candidatesCategories"
              :horizontal="false"
              :legend="true"
              :labelsYaxis="true"
              :distributed="false"
              :height="$q.platform.is.desktop ? '500px' : '300px'"
            />
          </div>
        </div>
      </q-card-section>
    </q-card>

    <q-card class="q-pa-md per-race-page__votes">
      <q-card-section>
        <h1
          :class="
            $q.platform.is.desktop ? 'text-h6' : 'text-subtitle1 text-center'
          "
        >
          VOTOS POR RAÇA
        </h1>

        <div class="row justify-center">
          <div class="col-12">
            <bar-chart
              :series="votesSeries"
              :categories="votesCategories"
              :horizontal="false"
              :legend="true"
              :labelsYaxis="true"
              :distributed="false"
              :logarithmic="true"
              :height="$q.platform.is.desktop ? '500px' : '450px'"
            />
          </div>
        </div>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import { defineComponent, onMounted, ref } from "vue";
import StatisticsService from "../../services/StatisticsService";
import BarChart from "../../components/charts/BarChart.vue";
export default defineComponent({
  name: "PerRace",
  setup() {
    const candidatesSeries = ref([]);
    const candidatesCategories = ref([]);

    const votesSeries = ref([]);
    const votesCategories = ref([]);

    function getByRace() {
      StatisticsService.getByRace().then((response) => {
        console.log(response);
        candidatesCategories.value = response.map((item) => item.ano);
        candidatesSeries.value = [
          {
            name: "Negros",
            data: response.map(
              (item) => item.qtd_candidatos[0].candidatosPretos
            ),
          },
          {
            name: "Brancos",
            data: response.map(
              (item) => item.qtd_candidatos[1].candidatosBrancos
            ),
          },
          {
            name: "Pardos",
            data: response.map(
              (item) => item.qtd_candidatos[2].candidatosPardos
            ),
          },
        ];
        candidatesCategories.value.pop();
        candidatesSeries.value.forEach((v) => {
          v.data.pop();
        });

        votesCategories.value = response.map((item) => item.ano);
        //apaga o ultimo elemento
        votesCategories.value.pop();
        votesSeries.value = [
          {
            name: "Brancos",
            data: response.map((item) => item.qtd_votos[0].votosBrancos),
          },
          {
            name: "Negros",
            data: response.map((item) => item.qtd_votos[1].votosPretos),
          },
          {
            name: "Pardos",
            data: response.map((item) => item.qtd_votos[2].votosPardos),
          },
        ];
        votesSeries.value.forEach((v) => {
          v.data.pop();
        });
        console.log(votesSeries.value);
      });
    }
    onMounted(() => {
      getByRace();
    });
    return {
      votesSeries,
      votesCategories,
      candidatesSeries,
      candidatesCategories,
    };
  },
  components: {
    BarChart,
  },
});
</script>

<style lang="scss" scoped>
.per-race-page {
  @media (min-width: $breakpoint-sm) {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: repeat(3, auto);
    &__votes {
      grid-column: 2/4;
    }
  }
}
</style>
