import pytest
from modules.db import Database

db = Database()

@pytest.mark.task1
def test_database_connection(db_conn):
    assert db_conn.test_connection()

@pytest.mark.task1
@pytest.mark.parametrize('search_param', (db.get_random_record()))
def test_check_admin_with_parameter(db_conn, driver_conn, search_param):
    normalized_data_from_admin = driver_conn.search_filtered_records(search_param)
    data_from_db = db_conn.search_with_random_parameter(search_param)

    assert len(normalized_data_from_admin['product_name']) == len(data_from_db['product_name'])

    for param_name in normalized_data_from_admin:
        assert normalized_data_from_admin[param_name] == data_from_db[param_name]

@pytest.mark.task2
@pytest.mark.parametrize('parameter', [
    'Ajax Socket',
    'Ajax Hub',
    'Ajax HubKit',
    'Ajax CenterButton (2-gang) vertical [55]'
])
def test_socket_quantity(db_conn, driver_conn, parameter):
    res_from_db = db_conn.search_for_product(parameter)
    res_from_admin = driver_conn.get_quantity_for_product(parameter)
    assert res_from_db == res_from_admin

db.close()
