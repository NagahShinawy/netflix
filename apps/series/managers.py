from django.db import models
from .choices import PositionChoices


class BackendModelManager(models.Manager):
    def get_queryset(self):
        return (
            super(BackendModelManager, self)
                .get_queryset()
                .filter(position__iexact=PositionChoices.BACKEND)
        )


class FrontendModelManager(models.Manager):
    def get_queryset(self):
        return (
            super(FrontendModelManager, self)
                .get_queryset()
                .filter(position__iexact=PositionChoices.UI)
        )

# todo: how to filter developers to get team lead
# class TeamLeadModelManager(models.Manager):
#     def get_queryset(self):
#         return (
#             super(TeamLeadModelManager, self)
#             .get_queryset()
#             .filter(team_lead=self)
#         )
