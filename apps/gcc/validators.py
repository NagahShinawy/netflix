from datetime import date
from django.core.exceptions import ValidationError
from .constants import FUTURE_DATE_ERROR


def is_future_date(dob):
    if dob > date.today():
        raise ValidationError(FUTURE_DATE_ERROR)
    return dob
