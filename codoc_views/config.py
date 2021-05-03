#!/usr/bin/env python3
from codoc.service.graph import create_graph_of_module

from dotenv import load_dotenv

import sample, tests, codoc_views


def bootstrap(**kwargs):
    load_dotenv()
    return (
        create_graph_of_module(sample, **kwargs)
        | create_graph_of_module(tests, **kwargs)
        | create_graph_of_module(codoc_views, **kwargs)
    )
