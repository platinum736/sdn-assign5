#!/usr/bin/python

"""
This example shows how to create an empty Mininet object
(without a topology object) and add nodes to it manually.
"""

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():
    "Create an empty network and add nodes to it."
    net = Mininet( controller=RemoteController )
    info( '*** Adding controller\n' )
    net.addController( 'c0',ip='127.0.0.1',port=6633 )
    info( '*** Adding hosts\n' )
    Host_1 = net.addHost('Host_1', ip='10.0.1.10/24',defaultRoute='via 10.0.1.1',mac='00:00:00:00:00:01')
    Host_2 = net.addHost('Host_2', ip='10.0.2.10/24',defaultRoute='via 10.0.2.1',mac='00:00:00:00:00:02')
    Host_3 = net.addHost('Host_3', ip='10.0.3.10/24',defaultRoute='via 10.0.3.1',mac='00:00:00:00:00:03')
    Host_4 = net.addHost('Host_4', ip='192.168.0.22/24',defaultRoute='via 192.168.0.1',mac='00:00:00:00:00:04')
    info( '*** Adding switch\n' )
    Device_1 = net.addSwitch( 's1' )
    Device_2 = net.addSwitch( 's2' )
    info( '*** Creating links\n' )
    net.addLink( Host_1, Device_1 )
    net.addLink( Host_2, Device_1 )
    net.addLink( Host_3, Device_1 )
    net.addLink( Host_4, Device_2 )
    net.addLink( Device_1, Device_2  )
    info( '*** Starting network\n')
    net.start()
    info( '*** Running CLI\n' )
    CLI( net )
    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
