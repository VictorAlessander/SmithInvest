from .result_sts_invest import ResultStsInvest
from .extractor_sts_invest import ExtractorStsInvest
from smith.avaliator import Avaliator
from smith.chart.bar_chart import BarChart


class StatusInvest:
    def __init__(self, tickers, international):
        self.tickers = tickers
        self._database = None
        self._avaliator = None
        self._extrator = None
        self._result = None
        self.international = international

        if self.international:
            self.base_url = "https://statusinvest.com.br/acoes/eua/"
        else:
            self.base_url = "https://statusinvest.com.br/acoes/"

    def start(self):
        results = []
        for ticker in self.tickers:
            link = f"{self.base_url}{ticker}"
            self._avaliator = Avaliator(link)
            self._avaliator.avaliate()
            self._extractor = ExtractorStsInvest(self._avaliator.connect())

            results.append(self._extractor.parser(self.international))

        self._result = ResultStsInvest(results)

    def finish(self):
        bar_chart = BarChart(self._result.get_results())
        bar_chart.draw("group", "operating_revenue_profit.html")
