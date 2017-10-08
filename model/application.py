class Application(object):
	def __init__(self,driver):
		self.driver = driver

	def go_to_home_page(self):
		self.driver.get("http://localhost/php4dvd/")

	def login(self, user):
		driver = self.driver
		driver.find_element_by_id("username").clear()
		driver.find_element_by_id("username").send_keys(user.username)
		driver.find_element_by_name("password").clear()
		driver.find_element_by_name("password").send_keys(user.password)
		driver.find_element_by_name("submit").click()

	def logout(self):
		driver = self.driver
		driver.find_element_by_link_text("Log out").click()
		driver.switch_to_alert().accept()

	def add(self, user):
		driver = self.driver
		driver.find_element_by_link_text("Add movie").click()
		driver.find_element_by_name("name").clear()
		driver.find_element_by_name("name").send_keys(user.name)
		driver.find_element_by_name("year").clear()
		driver.find_element_by_name("year").send_keys(user.year)
		driver.find_element_by_id("submit").click()

	def remove(self):
		driver = self.driver
		driver.find_element_by_link_text("Remove").click()
		driver.switch_to_alert().accept()