"""
Bashar Levin
15/12/2022
Labb4
"""
from threading import Thread, Lock, Semaphore
from datetime import datetime
import time

read_lock = Semaphore(3)
write_lock = Lock();
antal_semaphore = int(read_lock._value)

def delay():
    time.sleep(2)


def lock_readers():
    for i in range(antal_semaphore):
        read_lock.acquire()


def open_readers():
    for i in range(antal_semaphore):
        read_lock.release()


def read():
    while(1):
        if(not write_lock.locked()):
            read_lock.acquire()
            date = datetime.now()
            print(f"Reading...{date}")
            read_lock.release()
            delay();


def write():
        while(1):
            write_lock.acquire()
            lock_readers();
            date = datetime.now()
            print(f"Writing...{date}")
            write_lock.release()
            open_readers()
            delay()


def write_revers():
    while(1):
        write_lock.acquire()
        lock_readers()
        date = str(datetime.now() )[::-1]
        print(f"Writing in revers...{date}")
        write_lock.release()
        open_readers();
        delay()


w1 = Thread(target = write)
w2 = Thread(target = write_revers)
r1 = Thread(target = read)
r2 = Thread(target = read)
r3 = Thread(target = read);

w1.start()
w2.start()
r1.start()
r2.start()
r3.start()
