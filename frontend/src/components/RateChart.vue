<template>
  <div class="chart-container">
    <canvas ref="chart"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)

export default {
  props: ['rates'],
  mounted() {
    this.createChart()
  },
  methods: {
    createChart() {
      const ctx = this.$refs.chart.getContext('2d')
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.rates.map(item => item.x),
          datasets: [{
            label: 'GBP/CNY汇率',
            data: this.rates.map(item => item.y),
            borderColor: 'rgba(255, 50, 50, 1)',
            tension: 0.4,
            pointRadius: 4,
            pointBackgroundColor: 'rgba(255, 50, 50, 1)'
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false },
            tooltip: {
              callbacks: {
                label: (context) => `¥${context.raw}`
              }
            }
          },
          scales: {
            x: {
              title: { display: true, text: '日期' }
            },
            y: {
              title: { display: true, text: '汇率' },
              min: 0,
              max: 1.2
            }
          }
        }
      })
    }
  }
}
</script>