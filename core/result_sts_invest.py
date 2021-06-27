from smith.abstracts.AbstractResult import AbstractResult


@AbstractResult.register
class ResultStsInvest(AbstractResult):
    def __init__(self, results):
        super(ResultStsInvest, self).__init__()
        self.results = results

    def get_results(self):
        return self.results

    def get_results_formated(self):
        pass
