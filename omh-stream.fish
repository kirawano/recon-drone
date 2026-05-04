#this guy streams using udp :D
gst-launch-1.0 libcamerasrc ! \
video/x-raw,width=640,height=480, format=NV12, framerate=15/1 ! \
videorate ! \
videoconvert ! \
timeoverlay font-desc="Monospace 30" shaded-background=true ! \
x264enc tune=zerolatency bitrate=3000 speed-preset=ultrafast ! \
'video/x-h264,level=(string)4'  ! \
queue ! \
h264parse config-interval=1000  ! \
rtph264pay aggregate-mode=zero-latency ! \
udpsink host=10.240.183.142 port=5000 buffer-size=5
