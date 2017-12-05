from mininet.topo import Topo
from mininet.net import Mininet

if __name__ == "__main__":
	net = Mininet(controller=RemoteController)
	
	# Create simple topo

    host1 = net.addHost('h1', mac='00:00:00:00:00:01', ip='10.0.0.1/24')
    host2 = net.addHost('h2', mac='00:00:00:00:00:02', ip='10.0.0.2/24')
	# add hosts
	switch1 = net.addSwitch( 's1' , protocols='OpenFlow13')
	switch2 = net.addSwitch( 's2' , protocols='OpenFlow13')
	# add links
    net.addLink(switch1, host1)
	net.addLink(switch2, host2)
	net.addLink(switch1, switch2)
	# start mininet
	net.build()

