import sys
import os
path=sys.argv[1]if len(sys.argv)>1 else "."
print(os.listdir(path))
