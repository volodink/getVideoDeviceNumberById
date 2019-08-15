from time import sleep
from getVideoDeviceNumberById import getVideoDeviceNumberById

# ==================================================
# argus
cam1_id = "1ddaa10e"
# uran-9
cam2_id = "7b33851"
# uav
cam3_id = "798c03c"
# ==================================================

print('generating start file ...')
sleep(1)

f = open('start.bat', 'w')
f.write('start cmd /c red5\n')
f.write('powershell sleep 10\n')
f.write('start cmd /c ffmpeg -analyzeduration 0 -f dshow -video_size 640x480 -framerate 30 -video_device_number ' +
        str(getVideoDeviceNumberById(cam1_id)) + ' -i video="USB2.0 PC CAMERA" -tune zerolatency -f flv rtmp://localhost/oflaDemo/cam1\n')
f.write('powershell sleep 10\n')
f.write('start cmd /c ffmpeg -analyzeduration 0 -f dshow -video_size 640x480 -framerate 30 -video_device_number ' +
        str(getVideoDeviceNumberById(cam2_id)) + ' -i video="USB2.0 PC CAMERA" -tune zerolatency -f flv rtmp://localhost/oflaDemo/cam2\n')
f.write('powershell sleep 10\n')
f.write('start cmd /c ffmpeg -analyzeduration 0 -f dshow -video_size 640x480 -framerate 30 -video_device_number ' +
        str(getVideoDeviceNumberById(cam3_id)) + ' -i video="USB2.0 PC CAMERA" -tune zerolatency -f flv rtmp://localhost/oflaDemo/cam3\n')
f.close()
