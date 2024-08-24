import pytest
from modules.db import Database
from modules.buffer_page import BufferPage


db = Database()
page = BufferPage()
page.login()

@pytest.mark.task2
def test_database_connection():
    assert db.test_connection()

@pytest.mark.task2
@pytest.mark.parametrize('parameter',('Ajax Socket','Ajax Hub','Ajax HubKit','Ajax CenterButton (2-gang) vertical [55]'))
def test_socket_quantity(parameter):
    res_from_db = db.search_for_product(parameter)
    res_from_admin = page.get_quantity_for_product(parameter)
    assert res_from_db==res_from_admin


