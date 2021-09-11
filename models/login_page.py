

from os import EX_TEMPFAIL


class LoginPage:
    def __init__(self, page):
        self.page = page
        


    async def email_field(self,email):
        await self.page.fill("[placeholder=\"user@company.com\"]",email)   

    async def password_field(self,password):
        await self.page.fill("[placeholder=\"password\"]",password)


    async def submit_button(self):
        await self.page.click("button:has-text(\"Log in\")")
    
    # async def navigate(self,website):
    #     await self.page.goto(website)
        
    async def submit_login_form(self, user):
        await self.email_field(user["username"])
        await self.password_field(user["password"])
        await self.submit_button()
