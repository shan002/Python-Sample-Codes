from msvcrt import getch
import re
import os

file_name = str(input('Subtitle file name(with full path): ')).strip('"')
newFileName = file_name.split('.srt')[0] + '_synced_' + '.srt'
print("New file will be named: " + newFileName)


def addTime(Time, miliseconds, sign):
    if sign == '-':
        miliseconds *= -1
    hour, minute, second, milisecond = map(int, re.split(':|,', Time))
    totalMs = milisecond + second * 1000 + minute * 60 * 1000 + hour * 60 * 60 * 1000 + miliseconds
    if totalMs < 0:
        totalMs = 0
    hour = totalMs // (60 * 60 * 1000)
    totalMs %= (60 * 60 * 1000)
    minute = totalMs // (60 * 1000)
    totalMs %= (60 * 1000)
    second = totalMs // 1000
    milisecond %= 1000

    newTime = str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2) + ',' + str(milisecond).zfill(3)
    return newTime


def main():
    ms, sign = str(input('Enter the number of ms you want to delay followed by a space and then a + or - sign: ')).split()
    ms = int(ms)
    with open(file_name, 'r', encoding="utf-8") as file, open(newFileName, 'w', encoding="utf-8") as newFile:
        for line in file:
            if '-->' in line:
                line = line.strip('\n')
                beginTime, endTime = line.split('-->')
                beginTime = addTime(beginTime.strip(), ms, sign)
                endTime = addTime(endTime.strip(), ms, sign)
                line = beginTime + ' --> ' + endTime + '\n'

            newFile.write(line)


main()
if '_synced_' in file_name:
    os.remove(file_name)
    os.rename(newFileName, file_name)
print("Subtitle synchronized successfully!\nPress any key to exit...");
getch()
