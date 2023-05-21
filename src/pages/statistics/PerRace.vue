<template>
  <q-page padding class="column justify-center">
    <q-card class="q-pa-md">
      <q-card-section>
        <q-toolbar>
          <q-toolbar-title>
            <h1 class="text-h6">Quantidade De Candidatos Por Raça</h1>
          </q-toolbar-title>
        </q-toolbar>
        <div class="row justify-center">
          <div class="col-12">
            <bar-chart
              :series="candidatesSeries"
              :categories="candidatesCategories"
              :horizontal="false"
              :legend="true"
              :labelsYaxis="true"
              :distributed="false"
            />
          </div>
        </div>
      </q-card-section>
    </q-card>

    <q-card class="q-pa-md">
      <q-card-section>
        <q-toolbar>
          <q-toolbar-title>
            <h1 class="text-h6">Quantidade Votos Por Raça</h1>
          </q-toolbar-title>
        </q-toolbar>
        <div class="row justify-center">
          <div class="col-12">
            <bar-chart
              :series="votesSeries"
              :categories="votesCategories"
              :horizontal="false"
              :legend="true"
              :labelsYaxis="true"
              :distributed="false"
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
        votesCategories.value = response.map((item) => item.ano);
        votesSeries.value = [
          {
            name: "Negros",
            data: response.map((item) => item.qtd_votos[0].votosBrancos),
          },
          {
            name: "Brancos",
            data: response.map((item) => item.qtd_votos[1].votosPretos),
          },
          {
            name: "Pardos",
            data: response.map((item) => item.qtd_votos[2].votosPardos),
          },
        ];
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

<style lang="scss" scoped></style>
