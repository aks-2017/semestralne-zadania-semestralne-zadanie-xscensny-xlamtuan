from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_0
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.lib.mac import haddr_to_bin
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types

from ryu.controller.handler import set_ev_cls
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.topology import event, switches
from ryu.topology.api import get_switch, get_link



class customLatency(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSIONS]

    def __init__(self, *args, **kwargs):
        super(customLatency, self).__init__(*args, **kwargs)
        self.topology_api_app = self
        # some other code could come here
    

    @set_ev_cls(event.EventSwitchEnter)
    def get_topology_data(self, ev):
        switch_list = get_switch(self.topology_api_app, None)
        switches=[switch.dp.id for switch in switch_list]
        links_list = get_link(self.topology_api_app, None)
        links=[(link.src.dpid,link.dst.dpid,{'port':link.src.port_no}) for link in links_list]
        # (srcNode, dstNode, port)
        self.logger.info(links)
        self.logger.info(switches)
    