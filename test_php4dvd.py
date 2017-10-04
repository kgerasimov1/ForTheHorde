from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import driver

def login(driver):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("submit").click()

def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()

def add(driver):
    driver.find_element_by_link_text("Add movie").click()
    driver.find_element_by_name("name").clear()
    driver.find_element_by_name("name").send_keys("Blade runner")
    driver.find_element_by_name("year").clear()
    driver.find_element_by_name("year").send_keys("1982")
    driver.find_element_by_id("submit").click()

def remove(driver):
    driver.find_element_by_link_text("Remove").click()
    driver.switch_to_alert().accept()

def test_login(driver):
    driver.get("http://localhost/php4dvd/")
    login(driver)
    logout(driver)

def test_add_film(driver):
    driver.get("http://localhost/php4dvd/")
    login(driver)
    add(driver)
    logout(driver)

def test_remove_film(driver):
    driver.get("http://localhost/php4dvd/")
    login(driver)
    add(driver)
    remove(driver)
    logout(driver)