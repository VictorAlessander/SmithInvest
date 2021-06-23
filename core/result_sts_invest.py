from smith.abstracts.AbstractResult import AbstractResult


@AbstractResult.register
class ResultStsInvestImpl(AbstractResult):
    def __init__(self, results):
        super(ResultStsInvestImpl, self).__init__()
        self.results = results

    def get_results(self):
        return self.results

    def get_results_formated(self):
        pass
