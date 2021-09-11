

from os import EX_TEMPFAIL, name
from playwright.async_api import async_playwright
from time import sleep
import sys


class Projectpage:
    def __init__(self, page):
        self.page = page
        


    async def add_project(self):
        await self.page.click("[data-action=add-project]")   

    async def project_name(self,name):
        await self.page.fill("#project-name",name)


    async def project_proceed(self):
        await self.page.click("#project-add")
    
    async def navigate(self,website):
        await self.page.goto(website)
    
    async def validate_project_existence(self,project_name):
        print(project_name)
        
        await self.page.click("text=" + project_name)
        
        

    def validate_project_dashboard(self):
        self.page.expect_navigation(url="**/projects")
        

        
        
        
    
    async def create_project_form(self, name):
        await self.add_project()
        await self.project_name(name)
        await self.project_proceed()
        



        
