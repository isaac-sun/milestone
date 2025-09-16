<template>
  <div class="container">
    <RateButton @fetch-data="handleFetchData" />
    <div v-if="showData" class="data-container">
      <h2>今日汇率 (GBP/CNY)</h2>
      <p>{{ currentRate }}</p>
      <RateChart :rates="rates" />
    </div>
  </div>
</template>

<script>
import RateButton from './components/RateButton.vue'
import RateChart from './components/RateChart.vue'

export default {
  components: { RateButton, RateChart },
  data() {
    return {
      showData: false,
      currentRate: 0,
      rates: []
    }
  },
  methods: {
    async handleFetchData() {
      try {
        const response = await axios.get('http://localhost:5000/api/rates')
        this.currentRate = response.data[0].rate
        this.rates = response.data.map(item => ({
          x: new Date(item.timestamp).toLocaleDateString('zh-CN'),
          y: item.rate
        }))
        this.showData = true
      } catch (error) {
        alert('数据加载失败，请重试')
      }
    }
  }
}
</script>