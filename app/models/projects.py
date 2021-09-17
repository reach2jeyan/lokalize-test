

from os import EX_TEMPFAIL, name, path, sync
from playwright.sync_api import sync_playwright
from playwright.sync_api import Browser





import pytest
import unittest


class Projects:
    def __init__(self, page):
        self.page = page
        

    @property
    def add_project(self):
        return self.page.wait_for_selector("[data-action=add-project]")

    @property
    def upload_files(self):
        return self.page.wait_for_selector("text=Upload files")

    @property
    def project_name(self):
        return self.page.wait_for_selector('[data-name="project-name"]')

    @property
    def project_more_button(self):
        return self.page.wait_for_selector(".dropdown-toggle .tooltip-holder .img")


    @property
    def add_first_key(self):
        return self.page.wait_for_selector("[aria-label=\"Add first key\"]")

    @property
    def key_name_field(self):
        return self.page.wait_for_selector("[placeholder=\"Key\"]")

    @property
    def key_save_button(self):
        return self.page.wait_for_selector("#btn_addkey")

    @property
    def key_platform(self):
        return self.page.wait_for_selector("#s2id_autogen8")

    @property
    def translation_key(self):
        return self.page.wait_for_selector("span:has-text(\"Empty\")")


    @property
    def acknowledge_delete(self):
        return self.page.wait_for_selector("text=Project deleted.")

    @property
    def translation_key(self):
        return self.page.wait_for_selector("text=python English Empty 0")

    @property
    def translation_key_field(self):
        return self.page.wait_for_selector("CodeMirror cm-s-default CodeMirror-wrap")

    def verify_project_page_after_creation(self):
        visibility = self.upload_files.is_visible()
        return visibility

    def verify_key_added(self):
        visibility = self.translation_key().is_visible()
        return visibility



    def print_response(self):
        return self.page.on("response",lambda response: print(response.json(),response.request.url))

        

    def validate_project_dashboard(self):
        self.page.expect_navigation(url="**/projects")

    def assert_projects_page(self):
        self.add_project.is_visible()


    def create_key(self, name,platform):
        self.add_first_key.click()
        self.key_name_field.fill(name)
        self.key_platform.fill(platform)
        self.page.keyboard.press("Enter")
        self.key_save_button.click()

    def add_translation_key(self,name):
        self.translation_key.click()
        self.translation_key_field.is_visible()
        self.translation_key_field.fill(name,force=True)

        

        
        
        
    
    # async def create_project_form(self, name):
    #     await self.add_project()
    #     await self.project_name(name)
    #     await self.project_proceed()
        



        
