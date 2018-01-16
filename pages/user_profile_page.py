from selenium.webdriver.common.by import By
from pages.internal_page import InternalPage
from pages.blocks.user_form import UserForm
from selenium.webdriver.support.select import Select

class UserProfilePage(InternalPage):

    def __init__(self, driver, base_url):
        super(UserProfilePage, self).__init__(driver, base_url)
        self.user_form = UserForm(self.driver, self.base_url)

    @property
    def username_field_is_visible(self):
        return self.is_element_visible((By.NAME, "username"))