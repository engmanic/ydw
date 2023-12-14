# sys2.py
#import sys
#args = sys.argv[1:]
#for i in args:
#    print(i.upper(), end=' ')
def up(*args) :
    for i in args:
        print(i.upper(), end=' ')
up(" hello", "world")
