from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_0
# from ryu.lib.mac import haddr_to_bin
from ryu.lib.packet import packet, ethernet, arp, ipv4, ipv6, icmp
from ryu.topology import event

import time

# from unigui.pygamedisplay import PygameDisplay
# from unigui.colorscheme import VSCode
# from unigui.widget import TextWidget

class Controller(app_manager.RyuApp):
    """
    An RYU OpenFlow controller that knows the global network topology and can route
    packets in order to load-balance the network.
    """
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        super(Controller, self).__init__(*args, **kwargs)
        # TODO
        self.running = True
        # We'll keep a running list of hosts and switches that are connected here
        self.switches = []
        # Keep a dictionary of hosts, mapping MAC address to the (switch_idx, port) tuple it's connected to
        self.hosts = {}
        # Kepp an ARP table, mapping MAC addresses to IP addresses
        self.arp_table = {}
        # self.gui = TextWidget("tw", 0, 0, 500, 500, colorscheme=VSCode.dark)
        # self.gui.set_value("hello")
        # self.display = PygameDisplay(500, 500)
        # self.display.show(self.gui)


    def add_flow(self, datapath, priority, match, actions, buffer_id=None):
        """
        Add a flow entry to a switch
        """
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        mod = parser.OFPFlowMod(datapath=datapath, priority=priority, match=match, actions=actions, hard_timeout=0, cookie=0, command=ofproto.OFPFC_ADD)
        datapath.send_msg(mod)

    @set_ev_cls(event.EventSwitchEnter)
    def _switch_enter_handler(self, ev):
        """
        Function called when a new switch connects to the controller.
        """
        # The "datapath" is the switch itself
        switch = ev.switch.dp
        # The "parser" is specific to this switch, used to format messages that we send to the switch
        parser = switch.ofproto_parser
        # Add the switch to our list
        if switch not in self.switches:
            self.switches.append(switch)
            # The reference code keeps the datapath and the id in separate lists.. why?

        # TODO: The reference code requests additional info from the switch here
        print("New switch connected. Total switches: {}".format(len(self.switches)))

    @set_ev_cls(event.EventSwitchLeave, MAIN_DISPATCHER)
    def _switch_leave_handler(self, ev):
        """
        Function called when a switch disconnects from the controller.
        """
        switch = ev.switch.dp
        if switch in self.switches:
            self.switches.remove(switch)
        else:
            print("Error: an unconnected switch is trying to disconnect!")

    @set_ev_cls(event.EventLinkAdd, MAIN_DISPATCHER)
    def _link_add_handler(self, ev):
        """
        Function called when a new link is detected by the controller.
        """
        # TODO
        return

    @set_ev_cls(event.EventLinkDelete, MAIN_DISPATCHER)
    def _link_delete_handler(self, ev):
        """
        Function colled when a link is removed from the network.
        """
        # TODO
        return

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        """
        Function called when an OpenFlow packet is received by the controller.
        """
        # First get the relevant data about the packet:
        msg = ev.msg
        datapath = msg.datapath
        switch_idx = -1
        if datapath in self.switches:
            switch_idx = self.switches.index(datapath)
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.in_port
        pkt = packet.Packet(msg.data)
        
        # Debug printing:
        print("\n[" + time.ctime() + "]: Got an OFPPacketIn message: {}".format(msg))
        print("    in_port is {}".format(in_port))
        print("    Packet contains the following protocols: ", end='')
        for p in pkt.protocols:
            print(p.protocol_name + ' ', end='')
        print('')
        print("    pkt is {}".format(pkt), end='\n\n')

        # Get the Ethernet header info
        eth = pkt.get_protocol(ethernet.ethernet)
        src = eth.src
        dst = eth.dst

        # Regardless of protocol type, add the host to our list
        if src not in self.hosts:
            self.hosts[src] = (switch_idx, in_port)
        print("self.hosts is {}".format(self.hosts))


        # For IPv6 packets, just drop the packet (by having an empty actions list)
        if pkt.get_protocol(ipv6.ipv6):
            print("Adding an IPv6 flow entry!")
            match = parser.OFPMatch(dl_type=eth.ethertype)
            actions = []
            self.add_flow(datapath, 0, match, actions)

        # For ARP packets
        _arp = pkt.get_protocol(arp.arp)
        if _arp:
            src_ip = _arp.src_ip
            dst_ip = _arp.dst_ip
            print("Adding an ARP flow entry!")
            match = parser.OFPMatch(dl_type=eth.ethertype)
            actions = [parser.OFPActionOutput(ofproto.OFPP_FLOOD)]
            self.add_flow(datapath, 0, match, actions)

        # For IPv4 Packets, do something else
        _ipv4 = pkt.get_protocol(ipv4.ipv4)
        if _ipv4:
            print("Adding an IPv4 flow entry!")
            match = parser.OFPMatch(dl_type=eth.ethertype)
            actions = [parser.OFPActionOutput(ofproto.OFPP_NORMAL)]  # TODO Fix the flood here
            self.add_flow(datapath, 0, match, actions)