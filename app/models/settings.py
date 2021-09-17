from os import EX_TEMPFAIL, name, path, sync
from playwright.sync_api import sync_playwright
from playwright.sync_api import Browser



class Settings:
    def __init__(self, page):
        self.page = page

    @property
    def delete_project_button(self):
        return self.page.wait_for_selector("text=Delete project")

    @property
    def settings_button(self):
        return self.page.wait_for_selector("a[role=\"menuitem\"]:has-text(\"Settings\")")

    @property
    def project_delete_confirmation_field(self):
        # return self.page.wait_for_selector(".bootbox-input bootbox-input-text form-control")
        return self.page.wait_for_selector(".bootbox-form .bootbox-input")
        # return self.page.wait_for_selector("text")

    @property
    def fetch_project_name(self):
        return self.page.wait_for_selector('[name="projectName"]')

    @property
    def confirm_delete(self):
        return self.page.wait_for_selector("button:has-text(\"Delete project\")")

    def delete_project(self, project_name):
        #This function is being called from the loop that deletes all the projects.
            # When deleting a name has to be entered to confirm, which is passed to this function
        self.settings_button.click()
        self.page.wait_for_load_state("networkidle")
        self.delete_project_button.click(force=True)
        self.project_delete_confirmation_field.fill(project_name)
        self.confirm_delete.click()
