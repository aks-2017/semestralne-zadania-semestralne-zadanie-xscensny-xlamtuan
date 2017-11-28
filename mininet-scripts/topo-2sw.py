from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import RemoteController
from mininet.term import makeTerm
from time import sleep
import subprocess

if '__main__' == __name__:
    net = Mininet(controller=RemoteController, link=TCLink)
	subprocess.Popen(["sudo", "tc", "qdisc", "add", "dev", "lo", "root", "netem", "delay", "13ms"])
	c0 = net.addController('c0', port=6633)

	h1 = net.addHost('h1')
	h1 = net.addHost('h2')

	# add hosts
	switch1 = net.addSwitch( 's1' , protocols='OpenFlow13')
	switch2 = net.addSwitch( 's2' , protocols='OpenFlow13')
	switch3 = net.addSwitch( 's3' , protocols='OpenFlow13')
	switch4 = net.addSwitch( 's4' , protocols='OpenFlow13')	
	# add links
	net.addLink( switch1, switch2, bw=100, delay='8ms')
	net.addLink( switch1, switch3, bw=100, delay='8ms')
	net.addLink( switch1, switch4, bw=100, delay='8ms')
	net.addLink( switch2, switch3, bw=100, delay='8ms')
	net.addLink( switch2, switch4, bw=100, delay='8ms')
	net.addLink( h1, switch1, bw=100, delay='10ms')
	net.addLink( h2, switch2, bw=100, delay='10ms')

	net.build()
    c0.start()	

	h1.cmd('ifconfig h1-eth0 192.168.10.10 netmask 255.255.255.0')
	h1.cmd('ip route add default via 192.168.10.1 dev h1-eth0')

	h2.cmd('ifconfig h2-eth0 192.168.20.10 netmask 255.255.255.0')
	h2.cmd('ip route add default via 192.168.20.1 dev h2-eth0')	

	switch1.start([c0])
	switch2.start([c0])
	switch3.start([c0])
	switch4.start([c0])	

	net.startTerms()

	CLI(net)

	net.stop()