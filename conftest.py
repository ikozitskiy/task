import pytest
from modules.buffer_page import BufferPage
from modules.db import Database


@pytest.fixture(scope='session')
def db_conn() -> Database:
    db = Database()
    yield db
    db.close()


@pytest.fixture(scope='module')
def driver_conn() -> BufferPage:
    driver = BufferPage()
    driver.login()
    yield driver
    driver.close()
