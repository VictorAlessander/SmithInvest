from bs4 import BeautifulSoup as BSoup
from smith.abstracts.AbstractExtractor import AbstractExtractor
from .utils.sanitizor import Sanitizor


@AbstractExtractor.register
class ExtractorStsInvestImpl(AbstractExtractor):
    def __init__(self, response):
        super(ExtractorStsInvestImpl, self).__init__()
        self.response = response

    def parser(self):
        results = []
        gross_profit_sanitized = []
        operating_costs_sanitized = []

        content = BSoup(self.response.text, "html.parser")

        dre_table = content.find(
            "div",
            attrs={
                "aria-label": "Grid com a demonstração do resultado do exercício (DRE)"
            },
        )

        dre_table_body = dre_table.find("tbody")

        gross_profit = dre_table_body.select("tr")[2]
        operating_costs = dre_table_body.select("tr")[3]

        for gross_profit_elements in gross_profit.find_all(
            "td", attrs={"class": "level-0 value text-right DATA"}
        ):
            gross_profit_value = gross_profit_elements.find(
                "span", attrs={"class": "d-block"}
            )
            gross_profit_sanitized.append(
                Sanitizor(gross_profit_value.text).sanitize()
            )

        for operating_costs_elements in operating_costs.find_all(
            "td", attrs={"class": "level-0 value text-right DATA"}
        ):
            operating_costs_value = operating_costs_elements.find(
                "span", attrs={"class": "d-block"}
            )
            operating_costs_sanitized.append(
                Sanitizor(operating_costs_value.text).sanitize()
            )

        results.append(gross_profit_sanitized)
        results.append(operating_costs_sanitized)

        gross_profit_sanitized_size = len(gross_profit_sanitized)
        operating_costs_sanitized_size = len(operating_costs_sanitized)

        operating_revenue_profit_values = []
        company_ticker = str.upper(self.response.url.split("/")[4])

        if gross_profit_sanitized_size == operating_costs_sanitized_size:
            for x in range(0, gross_profit_sanitized_size):
                operating_revenue_profit_values.append(
                    gross_profit_sanitized[x]
                    - abs(operating_costs_sanitized[x])
                )

        data_collected = dict(
            name=company_ticker,
            x_axis=["2020", "2019", "2018", "2017", "2016"],
            y_axis=operating_revenue_profit_values,
        )

        return data_collected
