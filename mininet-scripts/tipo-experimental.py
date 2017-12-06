#!/usr/bin/python

from mininet.topo import Topo
# from mininet.link import TCLink

class MyTopo(Topo):
	def __init__(self):

		Topo.__init__(self)

		host1 = self.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1')
		host2 = self.addHost('h2', mac='00:00:00:00:00:02', ip='10.0.0.2')

		switch1 = self.addSwitch('s1')
		switch2 = self.addSwitch('s2')

		self.addLink(switch2, host2)
		self.addLink(switch1, host1)
		self.addLink(switch1, switch2)

topos = {'mytopo': (lambda: MyTopo() )}
