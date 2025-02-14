# 无人机监控数字大屏

```node.js
pnpm dev
```

# 算法

```python
python main.py
```

# 无人机rtmp内网推流

```bat
# 流地址 rtmp://[host]:1935/live/home
.\nginx.exe -c conf\nginx-win-rtmp.conf
```

# 公网推流测试

```shell
ffmpeg -re -stream_loop -1 -i input.flv -c copy -f flv rtmp://47.98.33.192/live/stream

```

# 视频流公网推流(ffmpeg+nginx-rtmp)

```shell
ffmpeg -re -i rtmp://192.168.5.5:1935/live/home -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -acodec copy -f flv rtmp://47.98.33.192:1935/live/stream

ffmpeg -re -i rtmp://192.168.5.5:1935/live/stream -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -acodec copy -f flv rtmp://47.98.33.192:1935/live

# 转推flv
ffmpeg -re -i rtmp://192.168.5.5:1935/live/home -vcodec libx264 -preset:v ultrafast -tune:v zerolatency -acodec copy -f flv rtmp://47.98.33.192:1935/live/test
```

# flv公网地址

```shell
http://47.98.33.192:8081/live?port=1935&app=live&stream=test
```

![](./src/assets/images/test.png)
