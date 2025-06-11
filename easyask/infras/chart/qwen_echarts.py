from typing import List, Any, Dict

from easyask.infras.chart.chart import Chart


class QwenEcharts(Chart):
    def __init__(self, dataset: List[List[Any]], config: Dict = None):
        super().__init__(dataset, config)

    def get_options(self):
        pass
