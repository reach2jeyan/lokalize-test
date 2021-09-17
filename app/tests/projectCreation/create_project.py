# test_search.py
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
# Step 1 : Precondition : Check if there are no projects apart from sample projects.    
    # Implement it by checking if there is an empty placeholder text for no projects.
            #If yes, 
                # then proceed with text
            #If no,
                # then fetch all the inner text of data-name=project-name
                    #Iterate through project name delete through UI until default empty page is visible

    #Test steps:
        # 1. When add project 
        # Write required fields
        # Check if this one project exists
        # Check if the data_name == 1 for `project-name`
    


class TestProjectcreation:
    @pytest.fixture(autouse=True)
    def setUp(self,page: Page):
            # Ideally we do not want to login each time, we rather login once before start of tests and store the state as a JSON
            #     Then we have a new context with page and launch from the stored state.
            #         PENDING IMPLEMENTATION OF THE NEW_CONTEXT
        self.login = Login(page)
        self.login.navigate()
        self.login.submit_login_form(testdata["data"]["credentials"])

    def test_project_page_must_open_after_creation(self,page):
        self.projects_page = ProjectDashboard(page)
        self.project_page = Projects(page)
        self.projects_page.verify_if_project_exists(page)
        self.projects_page.create_project(testdata["data"]["projectNames"]["firstProject"])
        page.wait_for_load_state("networkidle")
        assert self.project_page.verify_project_page_after_creation() == True

    def test_project_dashboard_contain_only_this_project(self,page):
        self.projects_page = ProjectDashboard(page)
        self.projects_page.navigate()
        assert self.projects_page.verify_number_of_projects() == 1

    def test_project_dashboard_contain_only_two_projects_in_correctorder(self, page):
        self.projects_page = ProjectDashboard(page)
        self.projects_page.create_project(testdata["data"]["projectNames"]["secondProject"])
        self.projects_page.navigate()
        assert self.projects_page.verify_number_of_projects() == 2
        assert self.projects_page.verify_order() == testdata["data"]["projectNames"]["firstProject"]


    
        