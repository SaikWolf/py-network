
import pytest
from test_import import load_em
load_em()
import pynet

import time


def make_send_tcp():
    return pynet.BetterConnection(pynet.SEND | pynet.TCP_ | pynet.BIND, '127.6.6.6', 6666).connect()
def make_recv_tcp():
    return pynet.BetterConnection(pynet.RECV | pynet.TCP_, '127.6.6.6', 6666).connect()

def make_send_udp():
    return pynet.BetterConnection(pynet.SEND | pynet.UDP_ | pynet.BIND, '127.6.6.6', 6667).connect()
def make_recv_udp():
    return pynet.BetterConnection(pynet.RECV | pynet.UDP_, '127.6.6.6', 6667).connect()


#defaults to tcp
def make_send_mcast():
    return pynet.BetterConnection(pynet.SEND | pynet.MCST | pynet.BIND, '224.6.6.6', 6666).connect()
def make_recv_mcast():
    return pynet.BetterConnection(pynet.RECV | pynet.MCST | pynet.BIND, '224.6.6.6', 6666).connect()


def make_send_mcast_udp():
    return pynet.BetterConnection(pynet.SEND | pynet.MCST | pynet.UDP_ | pynet.BIND, '224.6.6.6', 6667).connect()
def make_recv_mcast_udp():
    return pynet.BetterConnection(pynet.RECV | pynet.MCST | pynet.UDP_ | pynet.BIND, '224.6.6.6', 6667).connect()


def make_send_recv_udp(offset=0):
    return pynet.BetterConnection(pynet.SEND | pynet.RECV | pynet.UDP_ |
        (pynet.BIND if offset else pynet.OFF_), '127.6.6.6', 6668+(1 if offset else 0)).connect()
def make_send_recv_tcp(offset=0):
    return pynet.BetterConnection(pynet.SEND | pynet.RECV | pynet.TCP_ |
        (pynet.BIND if offset else pynet.OFF_), '127.6.6.6', 6670+(1 if offset else 0)).connect()

def test_makem():
    make_send_tcp().close()
    make_recv_tcp().close()
    with pytest.raises(NotImplementedError):
        make_send_udp().close()
    with pytest.raises(NotImplementedError):
        make_recv_udp().close()
    make_send_mcast().close()
    make_recv_mcast().close()
    make_send_mcast_udp().close()
    make_recv_mcast_udp().close()
    with pytest.raises(NotImplementedError):
        make_send_recv_udp(0).close()
    with pytest.raises(NotImplementedError):
        make_send_recv_udp(1).close()
    make_send_recv_tcp(0).close()
    make_send_recv_tcp(1).close()

def test_tcp_pingpong():
    tx = make_send_tcp()
    rx = make_recv_tcp()

    # tx.connect()
    # rx.connect()
    print(tx._sock_type)
    print(rx._sock_type)
    tx.close()
    rx.close()

