from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, HANDSHAKE_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from time import time,sleep




class ProjectController(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(ProjectController, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
	self.switch_start = 0
	self.switch_ignore = 0
	self.switch_time = 0
	self.switch_ignore1_arp = 0
	self.switch_ignore2_arp = 0
	self.echo_request_a = 0
	self.echo_request_b = 0

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
	
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions, buffer_id=None):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        if buffer_id:
            mod = parser.OFPFlowMod(datapath=datapath, buffer_id=buffer_id,
                                    priority=priority, match=match,
                                    instructions=inst)
        else:
            mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                    match=match, instructions=inst)
        datapath.send_msg(mod)

    def send_echo_request(self, datapath, data):
	ofp_parser = datapath.ofproto_parser
	req = ofp_parser.OFPEchoRequest(datapath, data)
	self.logger.info("sending echo request to switch %s", datapath.id)
	if self.echo_request_a == 0:
	    self.echo_request_a = time()
	else:
	    self.echo_request_b = time()
	datapath.send_msg(req)


    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]

        dst = eth.dst
        src = eth.src

        swid = datapath.id
        self.mac_to_port.setdefault(swid, {})
	if eth.ethertype != ether_types.ETH_TYPE_ARP:
	    # ignore other than ARP packet
	    return

	# self.logger.info("ARP %s %s %s %s", swid, src, dst, in_port)

        # self.logger.info("switch number %s %s %s %s", swid, src, dst, in_port)
	
	if swid == 1:
	    self.logger.info('ARP packet at switch 1')
	    if self.switch_start == 0:
		if self.switch_ignore1_arp > 0:
		    self.switch_ignore1_arp -= 1
		    self.logger.info('ignore this packet')
	            self.logger.info('==============================')
		    return

		self.switch_ignore1_arp = 2
		self.switch_start = 1
		out_port = 2
		self.switch_time = time()
		# create and send packet to 2nd switch

	    elif self.switch_start == 2:
		data = msg.data
		self.send_echo_request(datapath, data)
		# write time of arrival of packet
		self.switch_time = time() - self.switch_time - self.echo_request_a
		self.logger.info('==============================')
		return 

	    elif self.switch_start == 1:
		# ignore this packet
		self.logger.info('ignore this packet')
		return

	elif swid == 2:
	    self.logger.info('ARP packet at switch 2')
	    if self.switch_start == 0:
		if self.switch_ignore2_arp > 0:
		    self.switch_ignore2_arp -= 1
		    self.logger.info('ignore this packet')
		    self.logger.info('==============================')
		    return

		self.switch_ignore2_arp = 2
		self.switch_start = 2
		out_port = 2
		self.switch_time = time()
		# create and send packet to 1st switch

	    elif self.switch_start == 1:
		data = msg.data
		self.send_echo_request(datapath, data)
		# write time of arrival of packet
		self.switch_time = time() - self.switch_time - self.echo_request_a
		self.logger.info('===============================')
		return

	    elif self.switch_start == 2:
		# ignore this packet
		self.logger.info("ignore this packet")
		return

	

        # learn a mac address to avoid FLOOD next time.
        # self.mac_to_port[swid][src] = in_port

	

        #if dst in self.mac_to_port[swid]:
        #    out_port = self.mac_to_port[swid][dst]
        #else:
        #    out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data

	self.send_echo_request(datapath, data)

        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                  in_port=in_port, actions=actions, data=data)
	# save time of sending the packet
	self.switch_time = time()
        datapath.send_msg(out)

   
    @set_ev_cls(ofp_event.EventOFPEchoReply, MAIN_DISPATCHER)
    def echo_reply_handler(self, ev):
	self.logger.info("recieved reply from switch, RTT is:")
	if self.echo_request_b == 0:
	    self.echo_request_a = (time() - self.echo_request_a)/2
	    self.logger.info("%f s",self.echo_request_a)
	else:
	    self.echo_request_b = (time() - self.echo_request_b)/2
	    self.logger.info("%f s", self.echo_request_b)
	    self.logger.info("++++\ndelay between switches is: %f s\n++++",self.switch_time - self.echo_request_b)
	    self.switch_time = 0
	    self.echo_request_a = 0
	    self.echo_request_b = 0
	    self.switch_start = 0
	    self.switch_ignore = 0
	    
