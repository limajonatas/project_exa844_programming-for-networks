<template>
  <div :class="height == undefined ? 'chart' : ''">
    <apexchart
      :height="height ?? (100 + 30 * categories.length) ^ 5"
      type="bar"
      :options="chartOptionsComputed"
      :series="series"
      :key="key"
    />
  </div>
</template>

<script>
import {
  defineComponent,
  reactive,
  ref,
  onMounted,
  watch,
  computed,
} from "vue";
import { useQuasar } from "quasar";
export default defineComponent({
  name: "BarChart",
  props: {
    title: {
      type: String,
      required: false,
    },
    height: {
      type: String,
      required: false,
    },
    series: {
      type: Array,
    },
    categories: {
      type: Array,
      required: true,
    },
    formatYaxis: {
      type: String,
      default: "currency",
    },
    horizontal: {
      type: Boolean,
      dafault: true,
    },
    distributed: {
      type: Boolean,
      default: true,
    },
    dataLabels: {
      type: Boolean,
      dafault: true,
    },
    labelsYaxis: {
      type: Boolean,
      dafault: false,
    },
    legend: {
      type: Boolean,
      dafault: true,
      required: true,
    },
    logarithmic: {
      type: Boolean,
      dafault: false,
    },
  },
  setup(props) {
    const key = ref(0);
    const q = useQuasar();
    const chartOptionsComputed = computed(() => {
      let aux = { ...chartOptions };
      if (aux.legend?.labels?.colors)
        aux.legend.labels.colors = q.dark.isActive ? "#fff" : "#000";

      if (aux.xaxis?.labels?.style?.colors)
        aux.xaxis.labels.style.colors = q.dark.isActive ? "#fff" : "#000";

      if (aux.plotOptions?.bar?.horizontal)
        aux.plotOptions.bar.horizontal = props.horizontal;

      if (aux.plotOptions?.bar?.distributed)
        aux.plotOptions.bar.distributed = props.distributed;

      if (aux.legend?.show) aux.legend.show = props.legend;
      if (aux.xaxis?.categories) aux.xaxis.categories = props.categories;
      aux.yaxis = {
        logarithmic: props.logarithmic,
        logBase: 2,
        labels: {
          show: props.labelsYaxis,
          style: {
            colors: q.dark.isActive ? "#fff" : "#000",
            cssClass: "text-xs",
          },
        },
      };
      return aux;
    });

    const chartOptions = reactive({
      chart: {
        type: "bar",
        redrawOnParentResize: true,
      },
      plotOptions: {
        bar: {
          barHeight: "100%",
          columnWidth: "70%",
          //endingShape: 'rounded',
          horizontal: props.horizontal,
          distributed: props.distributed,
          dataLabels: {
            position: "bottom",
          },
        },
      },
      dataLabels: {
        enabled: props.dataLabels,
        textAnchor: "start",
        style: {
          colors: ["#fff"],
        },
        offsetX: 0,
        dropShadow: {
          enabled: true,
        },
        formatter: function (val) {
          return val;
        },
      },
      legend: {
        show: props.legend,
        labels: {
          colors: q.dark.isActive ? "#fff" : "#000",
        },
      },
      stroke: {
        width: 1,
        colors: ["#fff"],
      },
      xaxis: {
        categories: [],
        labels: {
          rotateAlways: true,
          rotate: -20,
          //minWidth: 0,
          //maxWidth: 160,
          style: {
            colors: q.dark.isActive ? "#fff" : "#000",
            cssClass: "text-xs",
          },
        },
      },
      yaxis: {
        logarithmic: false,
        logBase: 2,
        labels: {
          show: props.labelsYaxis,
          style: {
            colors: q.dark.isActive ? "#fff" : "#000",
            cssClass: "text-xs",
          },
        },
      },
      tooltip: {
        custom: function ({ series, seriesIndex, dataPointIndex, w }) {
          return `<div style="background-color:${
            !props.distributed
              ? w.globals.colors[seriesIndex]
              : w.globals.colors[dataPointIndex]
          };" class="font-black text-white text-weight-bolder">
            <span> ${w.globals.labels[dataPointIndex]} : ${
            series[seriesIndex][dataPointIndex]
          }
            </span>
            </div>`;
        },
      },
    });

    watch(
      () => props.categories,
      () => {
        if (chartOptionsComputed.value.xaxis?.categories)
          chartOptionsComputed.value.xaxis.categories = props.categories;
        key.value += 1;
      }
    );

    onMounted(() => {
      if (chartOptionsComputed.value.xaxis?.categories)
        chartOptionsComputed.value.xaxis.categories = props.categories;
    });

    return {
      key,
      chartOptionsComputed,
    };
  },
});
</script>
<style lang="scss" scoped>
.chart {
  overflow-y: auto;
  overflow-x: hidden;
  max-height: 300px;
}
</style>
