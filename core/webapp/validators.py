from django.core.validators import BaseValidator


class CustomSummaryValidator(BaseValidator):
    def __init__(self, limit_value=10):
        message = 'Max length %(limit_value)s'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit):
        return value > limit

    def clean(self, value):
        return len(value)

class CustomDescriptionValidator(BaseValidator):
    def __init__(self, limit_value=10):
        message = 'Min length %(limit_value)s'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit):
        return value < limit

    def clean(self, value):
        return len(value)