import ntpath
import os
import sys

if __name__ == '__main__':
    files = sys.argv[1]
    with open(files) as file:
        for line in file.readlines():
            f = ntpath.basename(line)
            os.system('cp ' + line.strip() + ' ' + f.strip())
