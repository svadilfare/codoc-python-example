#!/usr/bin/env python3
import codoc.domain.model
from codoc.service.export.codoc_view import view
from codoc.service import filters


@view(
    label="Whole System",
)
def view_whole_system(graph):
    """
    This view shows the whole Sample system.

    You will be able to see all modules etc.

    Normally views like these will be too verbose, and
    we normally recommend that you try to break
    the system into smaller bits or atleast only show modules.

    The sample application, however, is pretty small so it's not that big an issue now.
    """
    return graph


@view(
    label="Module diagram",
)
def view_modules(graph):
    """
    This view shows the modules of the Sample system.
    """
    return filters.exclude_classes(filters.exclude_functions(graph))
