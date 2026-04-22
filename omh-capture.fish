gst-launch-1.0 tcpclientsrc host=10.42.0.1 port=5000 ! \
gdpdepay ! \
rtph264depay ! \
h264parse ! \
avdec_h264 ! \
autovideosink
