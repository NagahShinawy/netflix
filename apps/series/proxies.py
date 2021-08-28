from .models import Developer
from .managers import BackendModelManager, FrontendModelManager, TeamLeadModelManager


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
    objects = TeamLeadModelManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Team Lead"
        verbose_name = "Developer"
