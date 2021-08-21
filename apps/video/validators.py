from datetime import datetime
from django.core.exceptions import ValidationError


class MaxYearValidator:

    message = "Video Production Year Can Not Be in The Future"

    def __call__(self, year: int):
        if year > datetime.now().year:
            raise ValidationError(self.message)
        return year


