import threading
from threading import *

def cube(num):
    print("cube {}".format(num**3))
def sq(num):
    print("square {}".format(num**2))
#create threading
t1 = threading.Thread(target=sq,args=(9,))
t2 = threading.Thread(target=cube,args=(5,))

t1.start()
t2.start()

#wait until thread 1 is completely executed
t1.join()
#wait until thread 2 is completely executed
t2.join()

#both thread completely executed
print('done')
