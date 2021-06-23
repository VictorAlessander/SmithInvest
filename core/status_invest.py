from .result_sts_invest import ResultStsInvestImpl
from .extractor_sts_invest import ExtractorStsInvestImpl
from smith.avaliator import Avaliator
from smith.chart.bar_chart import BarChart


class StatusInvest:
    def __init__(self, tickers):
        self.tickers = tickers
        self._database = None
        self._avaliator = None
        self._extrator = None
        self._result = None

    def start(self):
        results = []
        for ticker in self.tickers:
            link = f"https://statusinvest.com.br/acoes/{ticker}"
            self._avaliator = Avaliator(link)
            self._avaliator.avaliate()
            self._extractor = ExtractorStsInvestImpl(self._avaliator.connect())
            results.append(self._extractor.parser())

        self._result = ResultStsInvestImpl(results)

    def finish(self):
        """
        name: company
        """
        bar_chart = BarChart(self._result.get_results())
        bar_chart.draw("group", "operating_revenue_profit.html")
