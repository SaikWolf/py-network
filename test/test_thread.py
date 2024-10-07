
import pytest
from test_import import load_em
load_em()
import pynet

import threading
import time

def worker(duration):
    _me_ = threading.current_thread()
    # print("_me_",_me_)
    start = time.time()
    if isinstance(_me_,pynet.BetterThread):
        should_i_stop = _me_.check_for_stop
    else:
        should_i_stop = lambda : False

    while time.time()-start < duration and not should_i_stop():
        time.sleep(1.0)

def test_thread():
    stall_for = 3.0#sec
    sleep_for = 0.5
    thread = threading.Thread(target=worker,args=(stall_for,))
    start_at = time.time()
    thread.start()
    # print(thread)
    time.sleep(sleep_for)
    thread.join()
    # print('duration:',time.time()-start_at)
    assert time.time() - start_at > stall_for

def test_better_thread():
    stall_for = 3.0#sec
    sleep_for = 0.5
    thread = pynet.BetterThread(target=worker,args=(stall_for,))
    start_at = time.time()
    thread.start()
    # print(thread)
    time.sleep(sleep_for)
    thread.stop("stop test")
    thread.join()
    # print('duration:',time.time()-start_at)
    assert time.time() - start_at < stall_for
    assert thread.reason == "stop test"

def test_wait_thread():
    stall_for = 3.0#sec
    sleep_for = 0.5
    thread = pynet.BetterThread(target=worker,args=(stall_for,))
    start_at = time.time()
    thread.start()
    # print(thread)
    time.sleep(sleep_for)
    thread.wait()
    thread.join()
    # print('duration:',time.time()-start_at)
    assert time.time() - start_at > stall_for

def test_stopwait_thread():
    stall_for = 3.0#sec
    sleep_for = 0.5
    thread = pynet.BetterThread(target=worker,args=(stall_for,))
    start_at = time.time()
    thread.start()
    # print(thread)
    time.sleep(sleep_for)
    assert thread.reason is None
    thread.stop("wait")
    thread.wait()
    assert thread.reason == "wait"
    thread.join()
    # print('duration:',time.time()-start_at)
    assert time.time() - start_at < stall_for


