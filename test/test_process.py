
import pytest
from test_import import load_em
load_em()
import pynet

import time
import multiprocessing as mp

def worker(duration):
    # print("_me_",_me_)
    start = time.time()
    should_i_stop = lambda : False

    while time.time()-start < duration:
        time.sleep(1.0)

def test_process():
    stall_for = 3.0#sec
    sleep_for = 0.5
    proc = mp.Process(target=worker,args=(stall_for,))
    start_at = time.time()
    proc.start()
    # print(proc)
    time.sleep(sleep_for)
    proc.join()
    # print('duration:',time.time()-start_at)
    assert time.time() - start_at > stall_for

def test_better_process():
    stall_for = 3.0#sec
    sleep_for = 0.5
    proc = pynet.BetterProcess(target=worker,args=(stall_for,))
    start_at = time.time()
    proc.start()
    # print(proc)
    time.sleep(sleep_for)
    proc.stop("stop test")
    proc.join()
    # print('duration:',time.time()-start_at)
    assert time.time() - start_at < stall_for
    assert proc.reason == "stop test"

def test_wait_process():
    stall_for = 3.0#sec
    sleep_for = 0.5
    proc = pynet.BetterProcess(target=worker,args=(stall_for,))
    start_at = time.time()
    proc.start()
    # print(proc)
    time.sleep(sleep_for)
    proc.wait()
    proc.join()
    # print('duration:',time.time()-start_at)
    assert time.time() - start_at > stall_for

def test_stopwait_process():
    stall_for = 3.0#sec
    sleep_for = 0.5
    proc = pynet.BetterProcess(target=worker,args=(stall_for,))
    start_at = time.time()
    proc.start()
    # print(proc)
    time.sleep(sleep_for)
    assert proc.reason is None
    proc.stop("wait")
    proc.wait()
    assert proc.reason == "wait"
    proc.join()
    # print('duration:',time.time()-start_at)
    assert time.time() - start_at < stall_for


