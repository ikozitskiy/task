import pytest


class TestBufferPage:

    @pytest.mark.task1
    @pytest.mark.parametrize('index', [0, 1, 2], indirect=True)
    def test_check_admin_with_parameter(
            self, index, random_params, db_conn, driver_conn) -> None:
        normalized_data_from_admin = driver_conn.search_filtered_records(index)
        data_from_db = db_conn.search_with_random_parameter(index)

        assert len(normalized_data_from_admin['product_name']) == len(
            data_from_db['product_name'])

        for param_name in normalized_data_from_admin:
            assert normalized_data_from_admin[param_name] == data_from_db[param_name]

    @pytest.mark.task2
    @pytest.mark.parametrize('parameter', [
        'Ajax Socket',
        'Ajax Hub',
        'Ajax HubKit',
        'Ajax CenterButton (2-gang) vertical [55]'
    ])
    def test_socket_quantity(self, db_conn, driver_conn, parameter) -> None:
        res_from_db = db_conn.search_for_product(parameter)
        res_from_admin = driver_conn.get_quantity_for_product(parameter)
        assert res_from_db == res_from_admin