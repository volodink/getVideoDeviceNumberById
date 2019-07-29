import subprocess
import argparse
from builtins import print

parser = argparse.ArgumentParser()

parser.add_argument('--id', help='video device id', action='store')

#print(parser.parse_args())

cp = subprocess.run('ffmpeg/bin/ffmpeg.exe -list_devices true -f dshow -i dummy', universal_newlines=True,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

data = [x.strip() for x in cp.stderr.split('\n')]

camera_names_line_numbers = {}
line_counter = 0
video_device_num = 0
for line in data:
    if 'USB2.0 PC CAMERA' in line:
        darr = [video_device_num, data[line_counter + 1]]
        camera_names_line_numbers[line_counter] = darr
        video_device_num += 1
    line_counter += 1

# for k in camera_names_line_numbers:
#     print(camera_names_line_numbers[k])

found = 0
for key in camera_names_line_numbers:
    if parser.parse_args().id in camera_names_line_numbers[key][1]:
        found = 1
        video_device_n = camera_names_line_numbers[key][0]
        break

if found == 0:
    print(-1)
else:
    print(video_device_n)

