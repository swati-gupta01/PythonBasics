'''Accessing lock in thread can prevent to share global variables
and thus preventing data curroption'''

#with lock - calling lock.accquire()
#while exiting - lock.release()
import threading

x= 0
count=1000000
lock=threading.Lock()

def addition():
    global x
    with lock:
        for i in range(count):
            x+=2

def addition2():
    global x
    with lock:
        for i in range(count):
            x+=4

def substract():
    global x
    with lock:
        for i in range(count):
            x -= 2

def substract2():
    global x
    with lock:
        for i in range(count):
            x -= 4

th1=threading.Thread(target=addition())
th3=threading.Thread(target=addition2())
th2=threading.Thread(target=substract())
th4=threading.Thread(target=substract2())

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()

print(x)

