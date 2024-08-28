import pytest
from typing import Tuple

from modules.buffer_page import BufferPage
from modules.db import Database
from modules.driver import Driver


@pytest.fixture(scope='session')
def db_conn() -> Database:
    db = Database()
    assert db.test_connection()
    yield db
    db.close()


@pytest.fixture(scope='module')
def driver_conn() -> BufferPage:
    driver_wrapper = Driver()
    driver_wrapper.start_browser(BufferPage.URL)
    buffer_page = BufferPage(driver_wrapper.driver)
    buffer_page.login()

    yield buffer_page
    driver_wrapper.close()


@pytest.fixture(scope='module')
def random_params(db_conn) -> Tuple[str, str, str]:
    return db_conn.get_random_record()


@pytest.fixture
def index(request, random_params) -> str:
    param_index = request.param
    return random_params[param_index]
