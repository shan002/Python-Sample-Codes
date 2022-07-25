import os
import re

videoname = []

for fileName in os.listdir():
    name, ext = os.path.splitext(fileName)
    if ext == '.srt':
        namePart = re.split('-13\s-\s|-\s|-|\.', name)[2]
        videoname.append(namePart)

# print(videoname)
videoFilename = []
i = 0
for fileName in os.listdir():
    name, ext = os.path.splitext(fileName)
    if ext != '.mp4':
        continue
    newname = name + ' - ' + videoname[i]
    videoFilename.append(newname)
    i += 1
    print(newname + ext)
    os.rename(fileName, newname + ext)

# print(videoFilename)
i = 0
for fileName in os.listdir():
    name, ext = os.path.splitext(fileName)
    if ext != '.srt':
        continue
    newname = videoFilename[i] + ext
    i += 1
    print(newname)
    os.rename(fileName, newname)
