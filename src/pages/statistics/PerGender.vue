<template>
  <q-page padding class="per-gender-page">
    <q-card class="q-pa-md per-gender-page__candidates">
      <q-card-section>
        <h1
          :class="
            $q.platform.is.desktop ? 'text-h6' : 'text-subtitle1 text-center'
          "
        >
          Quantidade De Candidatos Por Genêro
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

    <q-card class="q-pa-md per-gender-page__votes">
      <q-card-section>
        <h1
          :class="
            $q.platform.is.desktop ? 'text-h6' : 'text-subtitle1 text-center'
          "
        >
          Quantidade Votos Por Genêro
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

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import StatisticsService from "../../services/StatisticsService";
import BarChart from "../../components/charts/BarChart.vue";
export default defineComponent({
  name: "PerGender",
  setup() {
    const candidatesSeries = ref([]);
    const candidatesCategories = ref([]);

    const votesSeries = ref([]);
    const votesCategories = ref([]);

    function getByGender() {
      StatisticsService.getByGender().then((response) => {
        console.log(response);
        candidatesCategories.value = response.map((item) => item.ano);
        candidatesSeries.value = [
          {
            name: "Feminino",
            data: response.map(
              (item) => item.qtd_candidatos[0].candidatosFemininos
            ),
          },
          {
            name: "Masculino",
            data: response.map(
              (item) => item.qtd_candidatos[1].candidatosMasculinos
            ),
          },
        ];
        votesCategories.value = response.map((item) => item.ano);
        votesSeries.value = [
          {
            name: "Feminino",
            data: response.map((item) => item.qtd_votos[0].votosFemininos),
          },
          {
            name: "Masculino",
            data: response.map((item) => item.qtd_votos[1].votosMasculinos),
          },
        ];
      });
    }
    onMounted(() => {
      getByGender();
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
.per-gender-page {
  @media (min-width: $breakpoint-sm) {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: repeat(5, auto);
    &__votes {
      grid-column: 2/6;
    }
  }
}
</style>
