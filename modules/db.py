import mysql.connector
import os

class Database():
    def __init__(self):
        self.connection = mysql.connector.connect(host=os.getenv('DB_URL'),
                     port=3306,
                     user=os.getenv('DB_USR'),
                     passwd=os.getenv('DB_PWD'),
                     db="production")
        self.cursor = self.connection.cursor()

    def close(self):
        if self.cursor is not None:
            self.cursor.close()

    def test_connection(self):
        query = 'SELECT VERSION()'
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_random_record(self):
        query = ('SELECT * FROM debug_production.buffer_one_c_products_record '
                             'where deactivation_time is null and approve_time is null ORDER BY RAND() LIMIT 1')
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record[0][4],record[0][2],record[0][1]

    def search_with_random_parameter(self,parameter):
        words = parameter.split()
        conditions = [
            f"(product_name LIKE '%{word}%' OR "
            f"bar_code LIKE '%{word}%' OR "
            f"vendor_code LIKE '%{word}%')"
            for word in words
        ]
        conditions_string = " AND ".join(conditions)
        query = f"SELECT * FROM debug_production.buffer_one_c_products_record WHERE " \
                f"approve_by_id IS NULL AND deactivation_time IS NULL AND " \
                f"{conditions_string} ORDER BY id DESC"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def search_for_product(self,parameter):
        query = ('SELECT * FROM debug_production.buffer_one_c_products_record '
                 f'where deactivation_time is null and approve_time is null and product_name = "{parameter}"')
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return len(record)
