from model.user import User
# from selenium_fixture import app

def test_login(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()

def test_remove_film(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.add(User.RemoveFilm())
    app.remove()

def test_add_film(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.add(User.AddFilm())