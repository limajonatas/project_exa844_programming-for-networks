<template>
  <q-page padding class="column justify-center">
    <q-card class="q-pa-md">
      <q-card-section>
        <q-toolbar>
          <q-toolbar-title>
            <h1 class="text-h6">
              Quantidade De Candidatos Por Grau De Instrução
            </h1>
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
              height="500px"
            />
          </div>
        </div>
      </q-card-section>
    </q-card>

    <q-card class="q-pa-md">
      <q-card-section>
        <q-toolbar>
          <q-toolbar-title>
            <h1 class="text-h6">Quantidade Votos Por Grau De Instrução</h1>
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
              :logarithmic="true"
              height="500px"
            />
          </div>
        </div>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import StatisticsService from "../../services/StatisticsService";
import BarChart from "../../components/charts/BarChart.vue";
export default defineComponent({
  name: "PerEducation",
  setup() {
    const candidatesSeries = ref([]);
    const candidatesCategories = ref([]);

    const votesSeries = ref([]);
    const votesCategories = ref([]);

    function getByEducation() {
      StatisticsService.getByEducation().then((response) => {
        console.log(response);
        candidatesCategories.value = response.map((item) => item.ano);
        candidatesSeries.value = [
          {
            name: "Ensino Fundamental Completo",
            data: response.map(
              (item) =>
                item.qtd_candidatos[0].candidatosEnsinoFundamentalCompleto
            ),
          },
          {
            name: "Ensino Médio Incompleto",
            data: response.map(
              (item) => item.qtd_candidatos[1].candidatosEnsinoMedioCompleto
            ),
          },
          {
            name: "Ensino Superior Incompleto",
            data: response.map(
              (item) =>
                item.qtd_candidatos[2].candidatosEnsinoSuperiorIncompleto
            ),
          },
          {
            name: "Ensino Superior Completo",
            data: response.map(
              (item) => item.qtd_candidatos[3].candidatosEnsinoSuperiorCompleto
            ),
          },
        ];
        votesCategories.value = response.map((item) => item.ano);
        votesSeries.value = [
          {
            name: "Ensino Fundamental Completo",
            data: response.map(
              (item) => item.qtd_votos[0].votosEnsinoFundamentalCompleto
            ),
          },
          {
            name: "Ensino Médio Incompleto",
            data: response.map(
              (item) => item.qtd_votos[1].votosEnsinoMedioCompleto
            ),
          },
          {
            name: "Ensino Superior Incompleto",
            data: response.map(
              (item) => item.qtd_votos[2].votosEnsinoSuperiorIncompleto
            ),
          },
          {
            name: "Ensino Superior Completo",
            data: response.map(
              (item) => item.qtd_votos[3].votosEnsinoSuperiorCompleto
            ),
          },
        ];
      });
    }
    onMounted(() => {
      getByEducation();
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
