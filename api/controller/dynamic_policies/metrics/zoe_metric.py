import json
from abstract_metric import Metric

class ZoeMetric(Metric):
    _sync = {}
    _async = ['attach', 'detach', 'notify', 'start_consuming', 'stop_consuming', 'init_consum', 'stop_actor']
    _ref = ['attach', 'detach']
    _parallel = []

    def __init__(self, name, exchange, queue, routing_key):
        Metric.__init__(self)

        self.exchange = exchange
        self.queue = queue
        self.routing_key = routing_key
        self.name = name

    def notify(self, body):
        """
        Method called from the consumer to indicate the value consumed from the
        rabbitmq queue. After receiving the value, this value is communicated to
        all the observers subscribed to this metric.

        e.g.:
            bd34c4073b65426894545b36f0d8dcce:gold
        """

        print "Zoe Metric - message received: " + body

        received_data = body.split(':')
        zoe_data = {"tenant": received_data[0], "abstract_policy": received_data[1].lower()}

        try:
            for observer in self._observers:
                observer.update(self.name, json.dumps(zoe_data))

        except Exception as e:
            print "Fail sending monitoring data to observer: ", e

    def attach(self, observer):
        """
        Asynchronous method. This method allows to be called remotely. It is
        called from observers in order to subscribe to this workload metric.
        This observer (the PyActive proxy) will be saved in a set structure.

        :param observer: The PyActive proxy of the observer that calls this method.
        :type observer: **any** PyActive Proxy type
        """
        print('Zoe Metric, Attaching observer: ' + str(observer))
        # tenant = observer.get_target()

        if not self._observers:
            self._observers = set()
        if observer not in self._observers:
            self._observers.add(observer)