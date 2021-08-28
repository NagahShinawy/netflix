from django.db import models
from .mixin import ModelRepMixin


class Task(ModelRepMixin, models.Model):
    title = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    developer = models.ForeignKey(
        "jira.Developer", on_delete=models.PROTECT, related_name="task"
    )
    desc = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    def to_pretty(self):
        return f"{self.title} {self.created}"


class Developer(ModelRepMixin, models.Model):
    name = models.CharField(max_length=256)
    tools = models.ManyToManyField(
        "jira.Tool", related_name="developers", null=True, blank=True
    )

    def __str__(self):
        return self.name.title()

    def to_pretty(self):
        return self

    def tasks(self):
        return [task.to_pretty() for task in self.task.all()]

    def tools_list(self):
        return [tool for tool in self.tools.all()]


class Tool(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def developers_list(self):
        return [developer for developer in self.developers.all()]
