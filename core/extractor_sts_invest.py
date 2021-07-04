from bs4 import BeautifulSoup as BSoup
from smith.abstracts.AbstractExtractor import AbstractExtractor
from .utils.sanitizor import Sanitizor


@AbstractExtractor.register
class ExtractorStsInvest(AbstractExtractor):
    DRE_TABLE_ATTRS = {
        "aria-label": "Grid com a demonstração do resultado do exercício (DRE)"
    }
    OP_REVENUE_PROFIT_ATTRS = {"class": "level-0 value text-right DATA"}
    OP_REVENUE_PROFIT_VALUE_ATTRS = {"class": "d-block"}
    GROSS_PROFIT_ATTRS = {"class": "level-0 value text-right DATA"}
    GROSS_PROFIT_VALUE_ATTRS = {"class": "d-block"}
    OPERATING_COSTS_ATTRS = {"class": "level-0 value text-right DATA"}
    OPERATING_COSTS_VALUE_ATTRS = {"class": "d-block"}
    YEARS = ["2020", "2019", "2018", "2017", "2016"]

    def __init__(self, response):
        super(ExtractorStsInvest, self).__init__()
        self.response = response

    def operating_revenue_profit(self, dre_table_body, company_ticker):
        op_revenue_profits = []
        op_revenue_profit_elements = dre_table_body.select("tr")[7]

        for element in op_revenue_profit_elements.find_all(
            "td", attrs=self.OP_REVENUE_PROFIT_ATTRS
        ):
            value = element.find(
                "span", attrs=self.OP_REVENUE_PROFIT_VALUE_ATTRS
            )
            sanitized_value = Sanitizor(value.text).sanitize()
            op_revenue_profits.append(sanitized_value)

        return dict(
            name=company_ticker, x_axis=self.YEARS, y_axis=op_revenue_profits
        )

    def gross_profit(self, dre_table_body):
        gross_profit_sanitized = []

        gross_profit = dre_table_body.select("tr")[2]

        for gross_profit_elements in gross_profit.find_all(
            "td", attrs=self.GROSS_PROFIT_ATTRS
        ):
            gross_profit_value = gross_profit_elements.find(
                "span", attrs=self.GROSS_PROFIT_VALUE_ATTRS
            )
            gross_profit_sanitized.append(
                Sanitizor(gross_profit_value.text).sanitize()
            )

        return gross_profit_sanitized

    def operating_costs(self, dre_table_body):
        operating_costs_sanitized = []

        operating_costs = dre_table_body.select("tr")[3]

        for operating_costs_elements in operating_costs.find_all(
            "td", attrs=self.OPERATING_COSTS_ATTRS
        ):
            operating_costs_value = operating_costs_elements.find(
                "span", attrs=self.OPERATING_COSTS_VALUE_ATTRS
            )
            operating_costs_sanitized.append(
                Sanitizor(operating_costs_value.text).sanitize()
            )

        return operating_costs_sanitized

    @staticmethod
    def calculate_operating_revenue_profit(
        gross_profit_values, operating_costs_values
    ):
        gross_profit_values_size = len(gross_profit_values)
        operating_costs_values_size = len(operating_costs_values)

        operating_revenue_profit_values = []

        if gross_profit_values_size == operating_costs_values_size:
            for x in range(0, gross_profit_values_size):
                operating_revenue_profit_values.append(
                    gross_profit_values[x] - abs(operating_costs_values[x])
                )

        return operating_revenue_profit_values

    def parser(self, international):
        results = []

        content = BSoup(self.response.text, "html.parser")

        dre_table = content.find(
            "div",
            attrs=self.DRE_TABLE_ATTRS,
        )

        dre_table_body = dre_table.find("tbody")

        # Verify if the respective url belongs to international sector
        # splitted_url_request = self.response.request.url.split("/")
        # if len(splitted_url_request) == 6:
        if international:
            company_ticker = str.upper(self.response.request.url.split("/")[5])

            return self.operating_revenue_profit(
                dre_table_body, company_ticker
            )

        gross_profit_values = self.gross_profit(dre_table_body)
        operating_costs_values = self.operating_costs(dre_table_body)

        results.append(gross_profit_values)
        results.append(operating_costs_values)

        company_ticker = str.upper(self.response.url.split("/")[4])

        operating_revenue_profit_values = (
            self.calculate_operating_revenue_profit(
                gross_profit_values, operating_costs_values
            )
        )

        return dict(
            name=company_ticker,
            x_axis=self.YEARS,
            y_axis=operating_revenue_profit_values,
        )
