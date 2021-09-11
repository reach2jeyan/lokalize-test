    


from playwright.async_api import async_playwright
from asyncio.runners import run
import sys
sys.path.insert(0,'..')

from models.login_page import LoginPage
from models.projects_page import Projectpage


import asyncio


class ProjectCreation:
    def create_project(self,name,url,file):
        async def main():
            async with async_playwright() as p:
                browser = await p.firefox.launch(headless=False)
                context = await browser.new_context(storage_state=file)
                page = await context.new_page()
                project_page = Projectpage(page)
                await page.goto(url)
                await project_page.create_project_form(name)
        
        asyncio.run(main())

    def validate_existence(self,name,url,file):
        async def main():
            async with async_playwright() as p:
                browser = await p.firefox.launch(headless=False,slow_mo=50)
                context = await browser.new_context(storage_state=file)
                page = await context.new_page()
                project_page = Projectpage(page)
                await page.goto(url)
                await project_page.validate_project_existence(name)
        
        asyncio.run(main())

    
        