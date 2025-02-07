import echarts from './chartInstall'
import type { ECOption } from './chartsInterface'

const chartInit = (mounted: HTMLDivElement, option: ECOption) => {
  const charts = echarts.init(mounted)
  charts.setOption(option)
  return charts
}

const changeOption = (charts: ReturnType<typeof chartInit>, option: ECOption) => {
  charts.setOption(option)
  return charts
}

export { chartInit, changeOption }
