import sys
import re

with open(sys.argv[1]) as f:
    for i in range(60):
        lines = f.readline()
        a = re.findall(r'\S+', lines)
        if i <9:
            print(a[2])
        else:
            print(a[2])
