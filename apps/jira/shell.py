from django.db.models import Count
from .models import Developer, Task, Tool

P = "p"


def p_tools():
    return Tool.objects.filter(name__istartswith=P)


def developers_use_p():
    return Developer.objects.filter(tools__name__istartswith=P)


# sort by max number of tools used of developer then by name in case of 2 or more developers have the same nums of tools
def top_developers():
    return Developer.objects.annotate(tool_count=Count("tools")).order_by(
        "-tool_count", "name"
    )
