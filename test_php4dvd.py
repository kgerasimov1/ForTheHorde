from model.user import User
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app

def test_login(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()

def test_remove_film(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.add(User.RemoveFilm())
    app.remove()
    app.logout()
    assert app.is_not_logged_in()

def test_add_film(app):
    app.go_to_home_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.add(User.AddFilm())
    app.logout()
    assert app.is_not_logged_in()