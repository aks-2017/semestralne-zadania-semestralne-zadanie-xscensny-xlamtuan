from mininet.topo import Topo
from mininet.net import Mininet

if __name__ == "__main__":
	net = Mininet(controller=RemoteController)
	
	# Create simple topo

		Topo.__init__( self )

        	host1 = self.addHost('h1')
        	host2 = self.addHost('h2')


    host1 = net.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24')
    host2 = net.addHost('h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24')
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

