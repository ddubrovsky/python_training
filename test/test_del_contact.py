__autor__ = 'Dmitrii Dubrovskii'
import pytest
from fixture.application_contact import ApplicationContact

@pytest.fixture
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_delete_first_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session_contact.logout()
