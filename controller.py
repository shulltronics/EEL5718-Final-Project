from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
# from ryu.lib.mac import haddr_to_bin
# from ryu.lib.packet import packet
from ryu.topology import event

# from unigui.pygamedisplay import PygameDisplay
# from unigui.colorscheme import VSCode
# from unigui.widget import TextWidget

class Controller(app_manager.RyuApp):
    """
    An RYU OpenFlow controller that knows the global network topology and can route
    packets in order to load-balance the network.
    """
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        super(Controller, self).__init__(*args, **kwargs)
        # TODO
        self.running = True
        # We'll keep a list of the switches that are connected here
        self.switches = []
        # self.gui = TextWidget("tw", 0, 0, 500, 500, colorscheme=VSCode.dark)
        # self.gui.set_value("hello")
        # self.display = PygameDisplay(500, 500)
        # self.display.show(self.gui)


    def add_flow(self, datapath, priority, match, actions, buffer_id=None):
        """
        Add a flow entry to a switch
        """
        # TODO
        return

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
        msg = ev.msg
        datapath = msg.datapath
        parser = datapath.ofproto_parser
        print("Got an OFPPacketIn message: {}".format(msg))