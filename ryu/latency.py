from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_3

from ryu.controller.handler import set_ev_cls
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER



class customLatency(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSIONS]

    def __init__(self, *args, **kwargs):
        super(customLatency, self).__init__(*args, **kwargs)
        # some other code could come here
    