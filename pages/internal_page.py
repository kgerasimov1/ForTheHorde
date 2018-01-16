from pages.page import Page
from selenium.webdriver.common.by import By


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_link_text("Log out")

    @property
    def add_movie_button(self):
        return self.driver.find_element_by_link_text("Add movie")

    @property
    def title_field(self):
        return self.driver.find_element_by_name("name")

    @property
    def year_field(self):
        return self.driver.find_element_by_name("year")

    @property
    def save_button(self):
        return self.driver.find_element_by_id("submit")

    @property
    def remove_button(self):
        return self.driver.find_element_by_link_text("Remove")

    # @property
    # def user_profile_link(self):
    #     return self.driver.find_element_by_name("My profile")

    @property
    def user_profile_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=profile']")

    @property
    def user_management_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=users']")

    # @property
    # def is_this_page(self):
    #     return self.is_element_visible((By.ID, "loginform"))

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

    @property
    def title_field_is_visible(self):
        # return self.wait.until(presence_of_element_located((By.NAME, "name")))
        return self.is_element_visible((By.NAME, "name"))