#this guy streams using udp :D
gst-launch-1.0 libcamerasrc ! \
video/x-raw,width=160,height=120, format=NV12, framerate=45/1 ! \
videorate ! \
#videoconvert ! \
timeoverlay font-desc="Monospace 30" shaded-background=true ! \
x264enc tune=zerolatency ! \
'video/x-h264,level=(string)4'  ! \
queue ! \
h264parse config-interval=1000  ! \
rtph264pay aggregate-mode=zero-latency ! \
udpsink host=192.168.0.14 port=5000 sync=false buffer-size=5
