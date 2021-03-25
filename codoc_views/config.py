#!/usr/bin/env python3
from codoc.service.graph import create_graph_of_module

from dotenv import load_dotenv

import sample
import tests


def bootstrap():
    load_dotenv()
    return create_graph_of_module(sample) | create_graph_of_module(tests)
