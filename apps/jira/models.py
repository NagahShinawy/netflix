from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    developer = models.ForeignKey("jira.Developer", on_delete=models.PROTECT, related_name="task")

    def __str__(self):
        return f"{self.title}"

    def to_pretty(self):
        return f"{self.title} {self.created}"


class Developer(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name.title()

    def tasks(self):
        return [task.to_pretty() for task in self.task.all()]