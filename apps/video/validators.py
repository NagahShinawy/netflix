from django.core.validators import MinValueValidator, MaxValueValidator


class MaxYearValidator(MaxValueValidator):
    message = f"Video Production Year Can Not Be In The Future. Max Is '%(limit_value)s'. Given '%(show_value)s'"


class MinYearValidator(MinValueValidator):
    message = f"Video Production Year Is Very Old. Min is '%(limit_value)s'. Given '%(show_value)s'"
