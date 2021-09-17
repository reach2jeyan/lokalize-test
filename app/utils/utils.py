import json
import sys

import pytest


class TestUtils:

    def __init__(self):
        pass

    def read_env(self,file_name):
        with open(file_name) as f:
            data = json.load(f)
            return data

# All the test utils will go here, like common actions or wait for network idle
