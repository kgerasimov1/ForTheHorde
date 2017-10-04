from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import driver

def login(driver, username, password):
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()

def logout(driver):
    driver.find_element_by_link_text("Log out").click()
    driver.switch_to_alert().accept()

def add(driver, name, year):
    driver.find_element_by_link_text("Add movie").click()
    driver.find_element_by_name("name").clear()
    driver.find_element_by_name("name").send_keys(name)
    driver.find_element_by_name("year").clear()
    driver.find_element_by_name("year").send_keys(year)
    driver.find_element_by_id("submit").click()

def remove(driver):
    driver.find_element_by_link_text("Remove").click()
    driver.switch_to_alert().accept()

def test_login(driver):
    driver.get("http://localhost/php4dvd/")
    login(driver, "admin", "admin")
    logout(driver)

def test_add_film(driver):
    driver.get("http://localhost/php4dvd/")
    login(driver, "admin", "admin")
    add(driver, "Blade runner", "1982")
    logout(driver)

def test_remove_film(driver):
    driver.get("http://localhost/php4dvd/")
    login(driver, "admin", "admin")
    add(driver, "Gladiator", "2000")
    remove(driver)
    logout(driver)