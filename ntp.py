import re

file_cisco = open('172.16.0.65.txt', 'r')

for line in file_cisco:
    pattern = re.compile('admin|test|remvord')
    pattern_ntp = re.compile('ntp server 192.168.120.50|ntp server 192.168.120.51')
    match = pattern.search(line)
    match_ntp = pattern_ntp.search(line)

# ntp server 192.168.168.192
# clock timezone MSK

    if match:
        print(match.group())
    elif match_ntp:
        print(match_ntp.group())
