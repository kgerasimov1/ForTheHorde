from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import driver

def test_login(driver):
    driver.get("http://localhost/php4dvd/")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("submit").click()
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()

def test_add_film(driver):
    driver.get("http://localhost/php4dvd/")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("submit").click()
    driver.find_element_by_link_text("Add movie").click()
    driver.find_element_by_name("name").clear()
    driver.find_element_by_name("name").send_keys("Blade runner")
    driver.find_element_by_name("year").clear()
    driver.find_element_by_name("year").send_keys("1982")
    driver.find_element_by_id("submit").click()
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()

def test_remove_film(driver):
    driver.get("http://localhost/php4dvd/")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("submit").click()
    driver.find_element_by_link_text("Add movie").click()
    driver.find_element_by_name("name").clear()
    driver.find_element_by_name("name").send_keys("Gladiator")
    driver.find_element_by_name("year").clear()
    driver.find_element_by_name("year").send_keys("2000")
    driver.find_element_by_id("submit").click()
    driver.find_element_by_link_text("Remove").click()
    driver.switch_to_alert().accept()
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()