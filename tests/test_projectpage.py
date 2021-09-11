# test_search.py

import sys
import pytest
import unittest

from asyncio.runners import run
from models import login_page
from models import projects_page
sys.path.insert(0,'..')

from models.login_page import LoginPage
from models.projects_page import Projectpage
from helper.login_action import StoreCookie

import asyncio
from playwright.async_api import Cookie, async_playwright
from helper.login_action import StoreCookie
from helper.create_project import ProjectCreation


user = {
        "username": "mrityunjeyan@sequoia.com",
        "password": "jeyy1988"
        }
name = {
    "project1": "automation"
}
environment = {
    "stage" : "https://stage.lokalise.com"
}
endpoint = {
    "project_dashboard": "/projects",
    "login_dashboard": "/login"
}


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(1)
        login_user = StoreCookie()
        login_user.user_login(user)
        
    def test_add_new_project(self):
        project_creation = ProjectCreation()
        project_creation.create_project(name,environment["stage"] + endpoint["project_dashboard"],"ownerUser.json")
        
    def test_verify_creation_in_dashboard(self):
        projects_page = ProjectCreation()
        projects_page.validate_existence(name["project1"],environment["stage"] + endpoint["project_dashboard"],"ownerUser.json")
        

        


    
        