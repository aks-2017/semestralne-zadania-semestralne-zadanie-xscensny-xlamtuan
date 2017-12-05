#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController, OVSSwitch
from mininet.node import Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet(topo=None, build=False , ipBase='10.10.0.0/24' , link=TCLink)

    info( '*** Adding controller\n' )
    net.addController( name='c0' , controller=RemoteController , ip='127.0.0.1', port=6653 )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.10.0.1' )
    h2 = net.addHost( 'h2', ip='10.10.0.2' )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1', cls=OVSSwitch )
    #s2 = net.addSwitch( 's2', cls=OVSSwitch )
    #s3 = net.addSwitch( 's3', cls=OVSSwitch )


    info( '*** Creating links\n' )
    net.addLink( h1, s1, delay='20ms' )
    net.addLink( h2, s1, delay='30ms' )

    # net.addLink( s1, s3, delay='0.25ms' )
    # net.addLink( s2, s3, delay='0.25ms' )
    # net.addLink( s1, s2, delay='0.25ms' )

    info( '*** Starting network\n')
    net.start()
    
    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
