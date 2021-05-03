#!/usr/bin/env python3
from codoc.service import filters
from codoc.service.export import view


@view(
    label="Module View",
)
def modules(graph):
    """
    This view contains all the top level modules that Sample contains.
    """
    module_graph = filters.include_only_modules(graph)
    top_module_graph = filters.get_depth_based_filter(2)(module_graph)
    return top_module_graph
