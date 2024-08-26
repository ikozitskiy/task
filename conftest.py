import pytest
from modules.buffer_page import BufferPage
from modules.db import Database


@pytest.fixture(scope='session')
def db_conn():
    db = Database()
    yield db
    db.close()


@pytest.fixture(scope='module')
def driver_conn():
    driver = BufferPage()
    driver.login()
    yield driver
    driver.close()
