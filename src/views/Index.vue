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
            <div class="boxnav" style="height: 300px">
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
              <li>安装设备：<span>N/A</span></li>
              <li>在线设备：<span>N/A</span></li>
            </ul>
          </div>

          <div class="box mapbox" style="overflow: hidden; position: relative">
            <div class="maptab">
              <!-- <a href="https://gitee.com/iGaoWei/big-data-view" class="active">地图</a> -->
              <a href="#">视频</a>
            </div>

            <!-- <div class="boxnav" id="map" style="height: 100%"></div> -->

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
              <!-- <ul class="clearfix">
              <li>
                <video
                  poster="images/face1.png"
                  src="http://www.17sucai.com/preview/1424582/2018-10-31/video/ckin.mp4
"
                  data-ckin="default"
                  data-overlay="1"
                  data-title="视频标题"
                ></video>
              </li>
              <li>
                <video
                  poster="images/face3.png"
                  src="http://www.17sucai.com/preview/1424582/2018-10-31/video/ckin.mp4
"
                  data-ckin="default"
                  data-overlay="1"
                  data-title="视频标题"
                ></video>
              </li>
              <li>
                <video
                  poster="images/face2.png"
                  src="http://www.17sucai.com/preview/1424582/2018-10-31/video/ckin.mp4
"
                  data-ckin="default"
                  data-overlay="1"
                  data-title="视频标题"
                ></video>
              </li>
              <li>
                <video
                  poster="images/head.jpg"
                  src="http://www.17sucai.com/preview/1424582/2018-10-31/video/ckin.mp4
"
                  data-ckin="default"
                  data-overlay="1"
                  data-title="视频标题"
                ></video>
              </li>
            </ul> -->
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
                <!-- <ul class="face02 clearfix">
                <li>
                  <div class="facedb">
                    <div><img src="images/face1.png" /></div>
                    <div><img src="images/face1.png" /></div>
                    <span>100%</span>
                  </div>
                  <p>姜文/A区正门</p>
                </li>
                <li>
                  <div class="facedb">
                    <div><img src="images/face1.png" /></div>
                    <div><img src="images/face1.png" /></div>
                    <span>100%</span>
                  </div>
                  <p>姜文/A区正门</p>
                </li>
                <li>
                  <div class="facedb">
                    <div><img src="images/face2.png" /></div>
                    <div><img src="images/face3.png" /></div>
                    <span>0%</span>
                  </div>
                  <p>姜文/A区正门</p>
                </li>

                <li>
                  <div class="facedb">
                    <div><img src="images/face1.png" /></div>
                    <div><img src="images/face2.png" /></div>
                    <span>99%</span>
                  </div>
                  <p>姜文/A区正门</p>
                </li>
                <li>
                  <div class="facedb">
                    <div><img src="images/face2.png" /></div>
                    <div><img src="images/face3.png" /></div>
                    <span>99%</span>
                  </div>
                  <p>姜文/A区正门</p>
                </li>
                <li>
                  <div class="facedb">
                    <div><img src="images/face2.png" /></div>
                    <div><img src="images/face1.png" /></div>
                    <span>99%</span>
                  </div>
                  <p>姜文/A区正门</p>
                </li>
                <li>
                  <div class="facedb">
                    <div><img src="images/face1.png" /></div>
                    <div><img src="images/face2.png" /></div>
                    <span>99%</span>
                  </div>
                  <p>姜文/A区正门</p>
                </li>
                <li>
                  <div class="facedb">
                    <div><img src="images/face1.png" /></div>
                    <div><img src="images/face2.png" /></div>
                    <span>99%</span>
                  </div>
                  <p>姜文/A区正门</p>
                </li>
              </ul> -->
              </div>
            </div>
          </div>
          <div class="box">
            <div class="tit"><span>到访次数</span></div>
            <div class="boxnav" ref="echart3" style="height: 300px"></div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { onMounted, ref, nextTick } from 'vue'
import { chartInit } from '@/hooks/useCharts'
import { pieOption, pieOption2, barOption } from '@/hooks/chartsOption'
//@ts-ignore
import flvjs from 'flv.js'

const flvPlayer = ref<any>(null)
const show = ref<boolean>(false)
const videoRef = ref<HTMLVideoElement | null>()
const echart1 = ref<HTMLDivElement | null>()
const echart2 = ref<HTMLDivElement | null>()
const echart3 = ref<HTMLDivElement | null>()

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
    // var videoElement = document.getElementById('videoElement')
    flvPlayer.value = flvjs.createPlayer({
      type: 'flv',
      url: 'http://47.98.33.192:8081/live?port=1935&app=live&stream=test', //你的url地址
      isLive: true,
      hasAudio: false,
    })
    flvPlayer.value.attachMediaElement(videoRef.value!)
    flvPlayer.value.load()

    setTimeout(function () {
      flvPlayer.value.play()
    }, 300)
    //处理视频播放错误的语法
    flvPlayer.value.on('error', () => {
      // message.error(`视频加载失败，请稍候重试！`);
      return false
    })
  }
}

onMounted(() => {
  // await nextTick()
  const charts1 = chartInit(echart1.value!, pieOption)
  const charts2 = chartInit(echart2.value!, pieOption2)
  const charts3 = chartInit(echart3.value!, barOption)
  createVideo()
  // console.log(charts1)
})
</script>

<style scoped lang="scss">
@import url('../assets/css/ckin.scss');
@import url('../assets/css/style.scss');
</style>
