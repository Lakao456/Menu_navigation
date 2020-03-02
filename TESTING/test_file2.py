import os
import sys
for i in os.listdir('..'):
    if '.py' not in i :
        print(i)
