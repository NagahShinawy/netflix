from .models import Developer
from .managers import BackendModelManager, FrontendModelManager


class FastEditDeveloperProxyModel(Developer):
    class Meta:
        proxy = True
        verbose_name_plural = "Fast Edit Developer"
        verbose_name = "Developer"


class BackendDeveloperProxyModel(Developer):

    objects = BackendModelManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Backend Developer"
        verbose_name = "Developer"


class FrontDeveloperProxyModel(Developer):

    objects = FrontendModelManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Frontend Developer"
        verbose_name = "Developer"


class TeamLeadProxyModel(Developer):
    class Meta:
        proxy = True
        verbose_name_plural = "Team Lead"
        verbose_name = "Developer"

    # todo: how to get team lead list
    # def tl_list(self):
    #     tl_ids = [dev.team_lead_id for dev in Developer.objects.all()]
    #     # return Developer.objects.filter(self.team_lead)
    #     return Developer.objects.filter(id__in=tl_ids)
