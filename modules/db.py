import mysql.connector
import os

from typing import List, Tuple


class Database:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host=os.getenv('DB_URL'),
            port=3306,
            user=os.getenv('DB_USR'),
            passwd=os.getenv('DB_PWD'),
            db='production'
        )
        self.cursor = self.connection.cursor()

    def close(self) -> None:
        if self.cursor is not None:
            self.cursor.close()

    def test_connection(self) -> str:
        query = 'SELECT VERSION()'
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        return record

    def get_random_record(self) -> tuple:
        query = (
            'SELECT * FROM debug_production.buffer_one_c_products_record '
            'WHERE deactivation_time IS NULL AND approve_time IS NULL '
            'ORDER BY RAND() LIMIT 1'
        )
        self.cursor.execute(query)
        record = self.cursor.fetchone()
        return record[4], record[2], record[1]

    def search_with_random_parameter(self, parameter) -> List[Tuple[any, ...]]:
        words = parameter.split()
        conditions = [
            f"(product_name LIKE '%{word}%' OR "
            f"bar_code LIKE '%{word}%' OR "
            f"vendor_code LIKE '%{word}%')"
            for word in words
        ]
        conditions_string = ' AND '.join(conditions)
        query = (
            f"SELECT * FROM debug_production.buffer_one_c_products_record "
            f"WHERE approve_by_id IS NULL AND deactivation_time IS NULL AND "
            f"{conditions_string} ORDER BY id DESC"
        )
        self.cursor.execute(query)
        column_names = [desc[0] for desc in self.cursor.description]
        rows = self.cursor.fetchall()
        result_dict = {col: [] for col in column_names}
        for row in rows:
            for col_name, value in zip(column_names, row):
                result_dict[col_name].append(value)
        return result_dict

    def search_for_product(self, parameter) -> int:
        query = (
            'SELECT * FROM debug_production.buffer_one_c_products_record '
            f'WHERE deactivation_time IS NULL AND approve_time IS NULL AND product_name = "{parameter}"'
        )
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return len(record)
