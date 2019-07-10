# import re
#
# word = open('172.16.0.65.txt', 'r')
#
# x = 0
#
# for line in word:
#     pattern = re.compile('username')
#     print(pattern.search(line)[1])
#     x += 1

# import re
#
# file_cisco = open('172.16.0.65.txt', 'r')
#
# for line in file_cisco:
#     pattern = re.compile('username')
#     match = pattern.search(line)
#
#     if match:
#         print(match.group)

#
import re

file3 = open('172.16.0.65.txt', 'r')
list3 = ['admin', 'remvord', 'test']

x = 0
for line in file3:
    if x <= len(list3) - 1:
        pattern = re.compile('username')
        match = pattern.search(line)

        if match:
            # print(list3[x])
            x += 1
            print(line[9:].strip())
