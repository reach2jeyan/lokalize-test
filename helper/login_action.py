
from playwright.async_api import async_playwright
from asyncio.runners import run
import sys
sys.path.insert(0,'..')

from models.login_page import LoginPage
from models.projects_page import Projectpage


import asyncio


class StoreCookie:
    def user_login(self,user,url):
        async def main():
                async with async_playwright() as p:
                    browser = await p.firefox.launch(headless=False)
                    context = await browser.new_context()
                    page = await context.new_page()
                    login_page = LoginPage(page)
                    project_page = Projectpage(page)
                    await self.page.goto(url)
                    await login_page.submit_login_form(user)
                    await project_page.add_project()
                    storage = await context.storage_state(path="ownerstate.json")
                

        asyncio.run(main())
        