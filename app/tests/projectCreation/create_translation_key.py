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

# Approach

            #Precondition
            # 1. A project with key must be created through an api or with backend before start of tests
            #Test Body
             # On the existing key created add a translation key

            #2(Followed here)
            # Check each time a project is there and if there, whether empty or not, is leading to lot of if,else
#                       thats not good in acceptance tests as it needs to be in control with clear state
            # So the process goes like this
                #Precondition
                    #1. When project exists, clear off all the projects and create a new project
                    #2. When new project created, then add key and ensure key exists
                #Test Body
                    # 1. Get inside the project created and create a translation key


#DISCLAIMER
# the translation input key is clickable but the field is not able to be filled, probably would be better to have a better element identifier to do this
                    #hence have kept it open

class TestTranslationKey:


    @pytest.fixture(autouse=True)
    def setUp(self, page: Page):
        self.projects_page = ProjectDashboard(page)
        self.project_page = Projects(page)
        self.login = Login(page)
        self.login.navigate()
        self.login.submit_login_form(testdata["data"]["credentials"])
        self.projects_page.verify_if_project_exists(page)
        self.projects_page.create_project(testdata["data"]["projectNames"]["firstProject"])
        self.project_page = Projects(page)
        self.project_page.create_key(testdata["keyName"]["firstKey"],testdata["platform"]["firstPlatform"])


    def test_should_be_ableto_add_translationkey(self, page):
        self.project_page = Projects(page)
        self.project_page.add_translation_key(testdata["translation"]["firstKey"])

