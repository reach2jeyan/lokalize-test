
from playwright.async_api import async_playwright
from asyncio.runners import run
import sys
sys.path.insert(0,'..')

from models.login import LoginPage
from models.projects_page import Projectpage


import asyncio


class StoreCookie:
    def user_login(self,user):
        async def main():
                async with async_playwright() as p:
                    browser = await p.firefox.launch(headless=False)
                    context = await browser.new_context()
                    page = await context.new_page()
                    login_page = LoginPage(page)
                    project_page = Projectpage(page)
                    await login_page.navigate("https://stage.lokalise.com/login")
                    await login_page.submit_login_form(user)
                    await project_page.new_project()
                    storage = await context.storage_state(path="state.json")
                    print(storage)
                    f = open("cookies.json","a")
                    f.write(storage)

        asyncio.run(main())