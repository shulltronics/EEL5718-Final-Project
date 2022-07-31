""" Custom topology example
One switch with server and client on either side:
   host --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

class StarTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topo."

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        hosts = [
            self.addHost('h1', ip='10.0.0.1/24'),
            self.addHost('h2', ip='10.0.0.2/24'),
            self.addHost('h3', ip='10.0.0.3/24'),
        ]
        # server.cmd('bash h2-server-setup.sh')
        switches = [
            self.addSwitch('s0'),
            # self.addSwitch('s1'),
        ]
        
        # Add links
        for host in hosts:
            self.addLink(host, switches[0])
        # for switch in switches:
        # self.addLink(switches[0], switches[1])

def network_test():
    topo = StarTopo()
    net = Mininet(topo, controller=None, autoSetMacs=True)
    print("Connecting to controller...")
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)
    print("Starting Mininet...")
    net.start()
    print("Dropping into mininet CLI...")
    CLI(net)

if __name__ == '__main__':
    setLogLevel('info')
    network_test()
