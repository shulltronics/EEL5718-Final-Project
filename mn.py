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
        hosts1 = [
            self.addHost('h1', ip='10.0.0.1/24'),
            self.addHost('h2', ip='10.0.0.2/24'),
            
        ]
        hosts2 = [
            self.addHost('h3', ip='10.0.0.3/24'),
            self.addHost('h4', ip='10.0.0.4/24'),
        ]
        hosts3 = [
            self.addHost('h5', ip='10.0.0.5/24'),
            self.addHost('h6', ip='10.0.0.6/24'),
        ]
        hosts4 = [
            self.addHost('h7', ip='10.0.0.7/24'),
            self.addHost('h8', ip='10.0.0.8/24'),
        ]
        # server.cmd('bash h2-server-setup.sh')
        switches = [
            self.addSwitch('s0'),
            self.addSwitch('s1'),
            self.addSwitch('s2'),
            self.addSwitch('s3'),
        ]
        
        # Add links
        for host in hosts1:
            self.addLink(host, switches[0])

        for host in hosts2:
            self.addLink(host, switches[1])

        for host in hosts3:
            self.addLink(host, switches[2])
        
        for host in hosts4:
            self.addLink(host, switches[3])

        self.addLink(switches[0], switches[1])
        self.addLink(switches[1], switches[2])
        self.addLink(switches[2], switches[3])


def network_test():
    topo = StarTopo()
    net = Mininet(topo, controller=None, autoSetMacs=True)
    print("Connecting to controller...")
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)
    print("Starting Mininet...")
    net.start()
    print("Dropping into mininet CLI...")
    CLI(net)

def default_test():
    topo = StarTopo()
    net = Mininet(topo, autoSetMacs=True)
    print("Starting Mininet...")
    net.start()
    print("Dropping into mininet CLI...")
    CLI(net)

if __name__ == '__main__':
    setLogLevel('info')
    network_test()
    # default_test()
