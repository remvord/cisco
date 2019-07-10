import difflib

file1 = open('172.16.0.1.txt', 'r')
file2 = open('172.16.0.1_old.txt', 'r')

diff = difflib.ndiff(file1.readlines(), file2.readlines())
delta = ''.join(x for x in diff if x.startswith('- '))

f = open('out_difference.txt', 'w')
f.write(delta)
f.close()

print(delta)
