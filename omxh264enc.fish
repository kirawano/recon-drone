#this guy streams using udp :D
gst-launch-1.0 libcamerasrc ! \
video/x-raw,width=192,height=108, format=NV12, framerate=45/1 ! \
videorate ! \
#videoconvert ! \
timeoverlay font-desc="Monospace 50" shaded-background=true ! \
v4l2h264enc extra-controls="controls,video_bitrate=1000000, insert-sps-pps=true" ! \
'video/x-h264,level=(string)4'  ! \
h264parse config-interval=-1  ! \
rtph264pay aggregate-mode=zero-latency ! \
udpsink host=10.39.118.205 port=5000 sync=false buffer-size=5
