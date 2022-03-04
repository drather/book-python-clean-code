import logging


class MetricClient:

    def send(self, metric_name, metric_value):
        if not isinstance(metric_name, str):
            raise TypeError("metric_name 으로 문자열 타입 사용해야 함")

        if not isinstance(metric_value, str):
            raise TypeError("metric_value 으로 문자열 타입 사용해야 함")

        logging.getLogger().info("metric_name, metric_value")


class Process:
    def __init__(self):
        self.client = MetricClient()

    def run_process(self):
        return 1

    def process_iterations(self, n_iterations):
        for i in range(n_iterations):
            result = self.run_process()
            self.client.send("iteration.".format(i), result)
