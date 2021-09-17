

from os import EX_TEMPFAIL
from playwright.sync_api import sync_playwright
import pytest



class Login:
    def __init__(self, page):
        self.page = page
        

    @property
    def email_field(self):
        return self.page.wait_for_selector("[placeholder=\"user@company.com\"]")
    @property
    def password_field(self):
        return self.page.wait_for_selector("[placeholder=\"password\"]")

    @property
    def submit_button(self):
        return self.page.wait_for_selector("button:has-text(\"Log in\")")



    def submit_login_form(self,user):
        
        self.email_field.fill(user["username"])
        self.password_field.fill(user["password"])
        self.submit_button.click()

    def navigate(self):
        self.page.goto("/login",wait_until="networkidle")

    def pourCookies(self,path):
        self.page.storageState({path:'state.json'})




