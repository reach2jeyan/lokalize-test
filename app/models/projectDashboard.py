from app.models.projects import Projects

from app.models.settings import Settings
from app.utils.utils import TestUtils

data = TestUtils()
testdata = data.read_env("app/tests/testdata.json")


class ProjectDashboard:
    def __init__(self, page):
        self.page = page

    @property
    def add_project_button(self):
        return self.page.wait_for_selector("[data-action=add-project]")

    @property
    def project_name_textfield(self):
        return self.page.wait_for_selector('#project-name')

    @property
    def project_proceed_button(self):
        return self.page.wait_for_selector("#project-add")

    @property
    def add_first_key(self):
        return self.page.wait_for_selector('[aria-label="Add first key"]')

    @property
    def key_editor_name(self):
        return self.page.wait_for_selector('#keyName')

    @property
    def key_editor_platforms(self):
        return self.page.wait_for_selector('#s2id_autogen8')

    @property
    def key_submit(self):
        return self.page.wait_for_selector('#btn_addkey')

    @property
    def empty_state(self):
        return self.page.wait_for_selector("img[alt=\"No projects.\"]")

    @property
    def project_name(self):
        return self.page.wait_for_selector('[data-name="project-name"]')

    @property
    def verify_project_empty(self):
        self.add_first_key.is_visible()

    @property
    def project_sidebar(self):
        return self.page.locator('[data-name="project-sidebar"]')

    def navigate(self):
        return self.page.goto("/projects")

    @property
    def project_more_button(self):
        return self.page.wait_for_selector(".dropdown-toggle .tooltip-holder .img")



    def verify_number_of_projects(self):
        #This returns the number of elements matching to that page
        button_count = self.project_sidebar.count()
        return button_count

    def create_project(self, name):
        self.add_project_button.click()
        self.project_name_textfield.fill(name)
        self.project_proceed_button.click()

    def verify_if_project_exists(self, page):
        #Clearing the projects until we see the empty state with the empty add project icon
            #When there are multiple projects, it will keep looping to delete them all
                #A very hacky way to do, ideally we can go about deleting all projects through the GET api of project,
                    # Get the project id and pass it as a header to the delete project.
                        # This was not straight forward and hence adopted to the UI way of precondition
        try:
            if self.project_name.is_visible():
                while self.project_name.is_visible():
                    self.delete_project_action(page)

        except:
            print("project cleared and in empty state.proceeding to test")

    def delete_project_action(self, page):
        self.settings_dashboard = Settings(page)
        project_name = self.project_name.inner_text()
        self.project_name.click()
        self.page.wait_for_load_state("networkidle")
        self.project_more_button.click()
        self.settings_dashboard.delete_project(project_name)

    def verify_order(self):
        # Returns the first name of the project created. Assert is being used with the same as test data.
        # But a better way to do this, is to get the count and loop until end and print all the names in a list
        project_name = self.project_name.inner_text()
        return project_name

