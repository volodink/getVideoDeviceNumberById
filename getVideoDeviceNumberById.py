import subprocess
from builtins import print

cp = subprocess.run('ffmpeg/bin/ffmpeg.exe -list_devices true -f dshow -i dummy', universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

data = [x.strip() for x in cp.stderr.split('\n')]

camera_names_line_numbers = []
line_counter = 0
for line in data:
    if 'USB2.0 PC CAMERA' in line:
        camera_names_line_numbers.append(line_counter)
    line_counter += 1


for number in camera_names_line_numbers:
    print(data[number])
    print(data[number+1])
