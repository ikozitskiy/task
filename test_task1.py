import pytest
from modules.db import Database
from modules.buffer_page import BufferPage


db = Database()
page = BufferPage()
page.login()

@pytest.mark.task1
def test_database_connection():
    assert db.test_connection()

@pytest.mark.task1
@pytest.mark.parametrize('search_param',(db.get_random_record()))
def test_check_admin_with_parameter(search_param):
    results = page.search_filtered_records(search_param)
    product_name_elements = results[0]
    guid_elements = results[1]
    vendor_elements = results[2]
    color_elements = results[3]
    barcode_elements = results[4]
    frequency_elements = results[5]
    country_elements = results[6]
    pro_acc_email_elements = results[7]
    pro_acc_name_elements = results[8]
    qr_box_elements = results[9]
    white_label_elements = results[10]
    ref_elements = results[11]
    pd_elements = results[12]
    distribution_channel_elements = results[13]
    status_elements = results[14]
    data_from_db = db.search_with_random_parameter(search_param)
    assert len(product_name_elements)==len(data_from_db)
    for point in range(len(data_from_db)):
        assert data_from_db[point][1] == product_name_elements[point].text
        assert data_from_db[point][2] == vendor_elements[point].text
        assert data_from_db[point][3] == (None if color_elements[point].text == '-' else color_elements[point].text )
        assert data_from_db[point][4] == barcode_elements[point].text
        assert data_from_db[point][5] == frequency_elements[point].text
        assert data_from_db[point][6] == (None if country_elements[point].text == '-' else country_elements[point].text)
        assert data_from_db[point][7] == (None if pro_acc_email_elements[point].text == '-' else pro_acc_email_elements[point].text)
        assert data_from_db[point][8] == (1 if white_label_elements[point].get_attribute('alt') == 'True' else 0)
        assert data_from_db[point][9] == (None if qr_box_elements[point].text == '-' else qr_box_elements[point].text)
        assert data_from_db[point][10] == (1 if ref_elements[point].get_attribute('alt') == 'True' else 0)
        assert data_from_db[point][13] == status_elements[point].text.lower()
        assert data_from_db[point][15] == (None if pro_acc_name_elements[point].text == '-' else pro_acc_name_elements[point].text)
        assert data_from_db[point][16] == (1 if pd_elements[point].get_attribute('alt') == 'True' else 0)
        assert data_from_db[point][19] == (None if guid_elements[point].text == '-' else guid_elements[point].text)
        assert data_from_db[point][21] == (None if distribution_channel_elements[point].text == '-' else distribution_channel_elements[point].text)


