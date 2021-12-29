from coin_data_manager.repositories.repository import AbstractRepository
from typing import List
import psycopg2 as pg


class Producer(AbstractRepository):
    def __init__(self, database, host, port, user, password):
        self.connection = pg.connect(
            database=database, host=host, port=port, user=user, password=password,
        )

    def add(self, model):
        pass

    def get(self, producer):
        cursor = self.connection.cursor()

        query = f"""
        SELECT id, market, unit, heartbeat, order
        FROM producer
        WHERE market = '{producer.market}' and unit = '{producer.unit}'
        """

        cursor.execute(query)
        producer = cursor.fetchall()[0]

        return producer

    def get_all(self) -> List:
        pass

    def update(self, model):
        pass

    def upsert(self, model):
        pass
