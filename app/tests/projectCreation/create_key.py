import sys
from unittest.suite import TestSuite
import pytest
import unittest
from app.models.login import Login

from app.models.projectDashboard import ProjectDashboard
from app.models.projects import Projects
from playwright.sync_api import Browser,Page
from app.utils.utils import TestUtils
#Read data from JSON file .
# The data is managed in the JSON file that will help to run with
#     various credentials and urls across
#             environments
data = TestUtils()
testdata = data.read_env("app/tests/testdata.json")

# Precondition
    # A project has to exist with empty key
        # Approach
        # 1. Have a precondition through api
                # 1. To create project


        # Test Body
            #Test if a key is able to be added inside the empty project
         #2(Followed here)
            # Check each time a project is there and if there, whether empty or not, is leading to lot of if,else
#                       thats not good in acceptance tests as it needs to be in control with clear state
            # So the process goes like this
                #1. When project exists, clear off all the projects and create a new project
                #2. When new project created, then add key and ensure key exists



class TestAddkey:
    @pytest.fixture(autouse=True)
    def setUp(self, page: Page):
        self.projects_page = ProjectDashboard(page)
        self.project_page = Projects(page)
        self.login = Login(page)
        self.login.navigate()
        self.login.submit_login_form(testdata["data"]["credentials"])
        self.projects_page.verify_if_project_exists(page)
        self.projects_page.create_project(testdata["data"]["projectNames"]["firstProject"])


    def test_should_be_able_to_add_key(self,page):
        self.project_page = Projects(page)
        # Alternatively we could standardize the JSON with a single key that could hold multiple keys
        self.project_page.create_key(testdata["data"]["keyName"]["firstKey"],testdata["data"]["platform"]["iOS"])
        assert self.project_page.verify_key_added() == True


