from abstract_metric import Metric
from metrics_parser import SwiftMetricsParse
class Get_Ops_Container(Metric):
    _sync = {}
    _async = ['get_value', 'attach', 'detach', 'notify', 'start_consuming','stop_consuming', 'init_consum', 'stop_actor']
    _ref = ['attach', 'detach']
    _parallel = []

    def __init__(self, exchange, queue, routing_key, host):
        Metric.__init__(self)

        self._host = host
        self.queue = queue
        self.routing_key = routing_key
        self.name = "get_ops_container"
        self.exchange = exchange
        self.parser_instance = SwiftMetricsParse()
        print 'Get ops tenant initialized'

    def notify(self, body):
        """
        PUT VAL swift_mdw/groupingtail-swift_metrics*4f0279da74ef4584a29dc72c835fe2c9*get_ops/counter interval=5.000 1448964179.433:198
        """
        body_parsed = self.parser_instance.parse(body)
        try:
            for observer in self._observers[body_parsed.target]:
                observer.update(self.name, body_parsed)
        except:
            print "fail", body_parsed
            pass

    def get_value(self):
        return self.value