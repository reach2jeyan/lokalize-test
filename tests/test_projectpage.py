# test_search.py

import sys
import pytest
import unittest

from asyncio.runners import run
sys.path.insert(0,'..')

from models.login import LoginPage
from models.projects_page import Projectpage

import asyncio
from playwright.async_api import Cookie, async_playwright
from helper.login_action import StoreCookie

# in the test
# async def main():
#     async with async_playwright() as p:
#         browser = await p.firefox.launch(headless=False)
#         context = await browser.new_context()
#         page = await context.new_page()
#         login_page = LoginPage(page)
#         project_page = Projectpage(page)
#         await login_page.navigate("https://stage.lokalise.com/login")
#         await login_page.submit_login_form(user)
#         await project_page.new_project()
#         storage = await context.storage_state(path="state.json")
#         print(storage)
#         f = open("cookies.json","a")
#         f.write(storage)

user = {
        "username": "mrityunjeyan@sequoia.com",
        "password": "jeyy1988"
        }



# class TestNewProject(object):
#     @pytest.fixture(scope='class')
#     def cookie(self):
#         fetch_cookie = StoreCookie()
#         fetch_cookie.user_login(user)
#     # async def main():
#     #     async with async_playwright() as p:
#     #         browser = await p.firefox.launch(headless=False)
#     #         context = await browser.new_context()
#     #         page = await context.new_page()
#     #         login_page = LoginPage(page)
#     #         project_page = Projectpage(page)
#     #         await login_page.navigate("https://stage.lokalise.com/login")
#     #         await login_page.submit_login_form(user)
#     #         await project_page.new_project()
#     #         storage = await context.storage_state(path="state.json")
#     #         print(storage)
#     #         f = open("cookies.json","a")
#     #         f.write(storage)

        

#     def test_new_project_creation(self):
#         self.test_new_project_creation
class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        fetch_cookie = StoreCookie()
        fetch_cookie.user_login(user)

    def test_add_new_project(self):
        self.test_add_new_project