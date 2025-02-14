<template>
  <div class="loading" v-if="show">
    <div class="loadbox"><img src="../assets/images/loading.gif" /> 页面加载中...</div>
  </div>
  <div class="all-container">
    <div class="mainbox">
      <ul class="clearfix nav1">
        <li style="width: 25%">
          <div class="box">
            <div class="tit"><span>实时抓拍人脸</span></div>
            <div class="boxnav">
              <div class="scolldiv scolldiv1">
                <ul class="face01 clearfix">
                  <li v-for="item in imageList">
                    <img :src="item.path" />
                    <p>姓名：{{ item.name }}</p>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div class="box">
            <div class="tit"><span>在岗工作人员</span></div>
            <div class="boxnav" style="height: 24.6rem">
              <table class="table1" width="100%" border="0" cellspacing="0" cellpadding="0">
                <tbody>
                  <tr>
                    <th>姓名</th>
                    <th>职位</th>
                    <th>当前签到次数</th>
                    <th>前一区间签到次数</th>
                  </tr>
                  <tr>
                    <td>张三</td>
                    <td>保安</td>
                    <td>3</td>
                    <td>5</td>
                  </tr>

                  <tr>
                    <td>张三</td>
                    <td>保安</td>
                    <td>3</td>
                    <td>5</td>
                  </tr>
                  <tr>
                    <td>张三</td>
                    <td>保安</td>
                    <td>3</td>
                    <td>5</td>
                  </tr>
                  <tr>
                    <td>张三</td>
                    <td>保安</td>
                    <td>3</td>
                    <td>5</td>
                  </tr>
                  <tr>
                    <td>张三</td>
                    <td>保安</td>
                    <td>3</td>
                    <td>5</td>
                  </tr>
                  <tr>
                    <td>张三</td>
                    <td>保安</td>
                    <td>3</td>
                    <td>5</td>
                  </tr>
                  <tr>
                    <td>张三</td>
                    <td>保安</td>
                    <td>3</td>
                    <td>5</td>
                  </tr>

                  <tr>
                    <td>张三</td>
                    <td>保安</td>
                    <td>3</td>
                    <td>5</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </li>
        <li style="width: 50%">
          <div class="tongji" style="height: 120px">
            <h1>时实客流量<span>N/A</span>人</h1>
            <ul>
              <li>对比次时昨日累计：<span>N/A</span>人</li>
              <li>同比增长：<span>N/A%</span></li>
              <li>安装设备：<span>1</span></li>
              <li>在线设备：<span>1</span></li>
            </ul>
          </div>

          <div class="box mapbox" style="overflow: hidden; position: relative">
            <div class="maptab">
              <a href="#">视频</a>
            </div>
            <div class="map_tool_outbox">
              <span class="map_tool">
                <a
                  href="https://gitee.com/iGaoWei/big-data-view"
                  class="map_tool_inner"
                  title="全图"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  href="https://gitee.com/iGaoWei/big-data-view"
                  class="map_tool_inner"
                  title="放大"
                  style="background-position-x: -36px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  href="https://gitee.com/iGaoWei/big-data-view"
                  class="map_tool_inner"
                  title="缩小"
                  style="background-position-x: -72px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner"
                  title="倒退视图"
                  style="background-position-x: -108px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner"
                  title="前进视图"
                  style="background-position-x: -144px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner display_type_btn"
                  title="专题地图"
                  style="background-position-x: -180px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner city_chose_btn"
                  title="城市定位"
                  style="background-position-x: -432px"
                ></a>
              </span>
              <span class="map_tool" id="btnBuffer">
                <a
                  class="map_tool_inner"
                  title="缓冲区分析"
                  style="background-position-x: -216px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner addition_check_btn check_btn"
                  title="地址检索"
                  style="background-position-x: -252px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner chemistry_check_btn check_btn"
                  title="危化品检索"
                  style="background-position-x: -288px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner enterprise_check_btn check_btn"
                  title="企业检索"
                  style="background-position-x: -324px"
                ></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner car_check_btn check_btn"
                  title="车辆检索"
                  style="background-position-x: -360px"
                ></a>
              </span>
              <span class="map_tool">
                <a class="map_tool_inner" title="搜索" style="background-position-x: -468px"></a>
              </span>
              <span class="map_tool">
                <a
                  class="map_tool_inner"
                  id="fresh_tool"
                  title="清空"
                  style="background-position-x: -396px"
                ></a>
              </span>
              <span class="map_tool">
                <input type="text" id="txtCoord" style="width: 150px; visibility: hidden" />
              </span>
            </div>

            <div class="boxnav">
              <video
                id="vid-eobo"
                ref="videoRef"
                style="width: 100%; height: 100%"
                class="vjs-default-skin video-js"
                autoplay
                controls
                preload="auto"
              ></video>
            </div>
          </div>
          <div>
            <div class="box" style="float: left; width: 49.5%; padding: 0 15px">
              <div class="tit"><span>男女比例</span></div>
              <div ref="echart1" style="height: 300px"></div>
            </div>
            <div class="box" style="float: right; width: 49.5%; padding: 0 15px">
              <div class="tit"><span>各年龄段比例</span></div>
              <div ref="echart2" style="height: 300px"></div>
            </div>
          </div>
        </li>
        <li style="width: 25%">
          <div class="box box2">
            <div class="tit"><span>目标人脸识别</span></div>
            <div class="boxnav">
              <div class="scolldiv scolldiv2">
                <Vue3SeamlessScroll :list="detectList" :step="step" class="scroll-container">
                  <ul class="scroll-list">
                    <li v-for="item in detectList">
                      <div>{{ item.name }}</div>
                      <div>{{ item.confidence }}</div>
                      <div>{{ item.position }}</div>
                    </li>
                  </ul>
                </Vue3SeamlessScroll>
              </div>
            </div>
          </div>
          <div class="box">
            <div class="tit"><span>到访次数</span></div>
            <div class="boxnav" ref="echart3" style="height: 24.6rem"></div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref, nextTick, computed } from 'vue'
import { chartInit } from '@/hooks/useCharts'
import { pieOption, pieOption2, barOption } from '@/hooks/chartsOption'
import { Vue3SeamlessScroll } from 'vue3-seamless-scroll'
//@ts-ignore
import flvjs from 'flv.js'

const step = ref<number>(0.8)
const flvPlayer = ref<any>(null)
const show = ref<boolean>(false)
const videoRef = ref<HTMLVideoElement | null>()
const echart1 = ref<HTMLDivElement | null>()
const echart2 = ref<HTMLDivElement | null>()
const echart3 = ref<HTMLDivElement | null>()

const detectList = ref<Record<'name' | 'confidence' | 'position', string>[]>([
  { name: '行人', confidence: '0.76', position: '' },
  { name: '行人', confidence: '0.64', position: '' },
  { name: '行人', confidence: '0.32', position: '' },
  { name: '行人', confidence: '0.89', position: '' },
  { name: '行人', confidence: '0.76', position: '' },
  { name: '行人', confidence: '0.64', position: '' },
  { name: '行人', confidence: '0.32', position: '' },
  { name: '行人', confidence: '0.89', position: '' },
  { name: '行人', confidence: '0.76', position: '' },
  { name: '行人', confidence: '0.64', position: '' },
  { name: '行人', confidence: '0.32', position: '' },
  { name: '行人', confidence: '0.89', position: '' },
])

const imageList = ref<Record<'path' | 'name', string>[]>([
  { path: 'src/assets/images/face1.png', name: '姜文' },
  { path: 'src/assets/images/face2.png', name: '刘德华' },
  { path: 'src/assets/images/face3.png', name: '周星驰' },
  { path: 'src/assets/images/face1.png', name: '姜文' },
  { path: 'src/assets/images/face2.png', name: '刘德华' },
  { path: 'src/assets/images/face3.png', name: '周星驰' },
])

const createVideo = () => {
  if (flvjs.isSupported()) {
    flvPlayer.value = flvjs.createPlayer({
      type: 'flv',
      url: 'http://47.98.33.192:8081/live?port=1935&app=live&stream=test',
      isLive: true,
      hasAudio: false,
    })
    flvPlayer.value.attachMediaElement(videoRef.value!)
    flvPlayer.value.load()

    setTimeout(function () {
      flvPlayer.value.play()
    }, 300)
    flvPlayer.value.on('error', () => {
      return false
    })
  }
}

onMounted(() => {
  const charts1 = chartInit(echart1.value!, pieOption)
  const charts2 = chartInit(echart2.value!, pieOption2)
  const charts3 = chartInit(echart3.value!, barOption)
  createVideo()
})
</script>

<style scoped lang="scss">
@import url('../assets/css/ckin.scss');
@import url('../assets/css/style.scss');
.scroll-container {
  width: 100%;
  height: 100%;
  .scroll-list {
    list-style: none;
    li {
      margin-top: 0.5rem;
      display: flex;
      div {
        width: 33.3%;
        text-align: center;
        &:nth-child(2) {
          font-family: electronicFont;
        }
      }
    }
  }
}
</style>
