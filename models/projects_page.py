

from os import EX_TEMPFAIL


class Projectpage:
    def __init__(self, page):
        self.page = page
        


    async def add_project(self):
        await self.page.click("[data-action=add-project]")   

    async def password_field(self,password):
        await self.page.fill("[placeholder=\"password\"]",password)


    async def submit_button(self):
        await self.page.click("button:has-text(\"Log in\")")
    
    async def navigate(self,website):
        await self.page.goto(website)
        
    async def new_project(self):
        await self.add_project()

        
