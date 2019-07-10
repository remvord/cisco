import difflib


def separate():
    file1 = open('append_new.txt', 'r')
    file2 = open('append_old.txt', 'r')

    diff = difflib.ndiff(file1.readlines(), file2.readlines())
    delta = ''.join(x for x in diff if x.startswith('- '))

    f = open('append_out.txt', 'w')
    f.write(delta)
    f.close()

    print(delta)
