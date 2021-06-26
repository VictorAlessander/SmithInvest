import re
from decimal import Decimal


class Sanitizor:
    def __init__(self, value):
        self.value = value

    def special_characters_remover(self):
        self.value = re.sub("[\t\n M]", "", self.value)
        return self.value

    def dot_remover(self):
        self.value = re.sub("[.]", "", self.value)
        return self.value

    def comma_handler(self):
        self.value = re.sub("[,]", ".", self.value)
        return self.value

    def sanitize(self):
        handlers = [
            self.special_characters_remover,
            self.dot_remover,
            self.comma_handler,
        ]

        sanitized_value = self.value

        # import pdb

        # pdb.set_trace()

        for handler in handlers:
            sanitized_value = handler()

        return Decimal(sanitized_value)
