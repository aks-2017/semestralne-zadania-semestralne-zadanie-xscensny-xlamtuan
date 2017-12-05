from mininet.topo import Topo

class MyTopo( Topo ):
	def __init__(self):
	#def build(self):
	# Create simple topo
		Topo.__init__( self )

        	host1 = self.addHost('h1')
        	host2 = self.addHost('h2')

	# add hosts
		switch1 = self.addSwitch( 's1', cls=OVSSwitch )
#		switch2 = self.addSwitch( 's2' )
#		switch3 = self.addSwitch( 's3' )
#		switch4 = self.addSwitch( 's4' )	
		# add links
	        self.addLink(host1, switch1, delay='20ms')
	        self.addLink(host2, switch1, delay='30ms')
#		self.addLink( switch1, switch2)
#		self.addLink( switch1, switch3)
#		self.addLink( switch1, switch4)
#		self.addLink(switch2, switch3)
#		self.addLink(switch2, switch4)

topos = { 'mytopo': MyTopo }
