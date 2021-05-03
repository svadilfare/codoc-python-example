#!/usr/bin/env python3
from codoc.service import filters
from codoc.service.export import view

import sample.simple


@view(
    label="Domain model (Classes)",
)
def domain_model_data_classes(graph):
    """
    This view shows the domain model of the Sample system.

    According to Wikipedia:
       In software engineering, a domain model is a
       conceptual model of the domain that
       incorporates both behavior and data

    This, however, only contains our actual data classes.

    We exclude our external dependencies, to get a cleaner graph
    """
    graph = filters.get_children_of(sample.simple, keep_external_nodes=False)(graph)

    return filters.include_only_classes(graph)
