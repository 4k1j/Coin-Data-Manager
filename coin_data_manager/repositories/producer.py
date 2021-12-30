from coin_data_manager.models.producer import Producer
from coin_data_manager.repositories.repository import AbstractRepository
from typing import List
import psycopg2 as pg


class NotFoundError(Exception):
    pass


class ProducerRepository(AbstractRepository):
    def __init__(self, database, host, port, user, password):
        self.connection = pg.connect(
            database=database, host=host, port=port, user=user, password=password,
        )

    def add(self, model):
        pass

    def get(self, producer) -> Producer:
        cursor = self.connection.cursor()

        query = f"""
        SELECT market, unit, heartbeat, order
        FROM producer
        WHERE market = '{producer.market}' and unit = '{producer.unit}'
        """

        cursor.execute(query)
        results = cursor.fetchall()
        if len(results) == 0:
            raise NotFoundError(f"Not found producer : {producer.market}:{producer.unit}")

        market, unit, heartbeat, order = results[0]

        return Producer(
            market, unit, heartbeat, order
        )

    def get_all(self) -> List:
        pass

    def update(self, producer: Producer):
        cursor = self.connection.cursor()

        query = f"""
        UPDATE producer
        SET market = '{producer.market}',
            unit = '{producer.unit}',
            heartbeat = '{producer.heartbeat}',
            order = '{producer.order}'
        
        WHERE market = '{producer.market}' AND unit = '{producer.unit}'
        """.replace("'None'", "NULL")

        cursor.execute(query)
        self.connection.commit()

    def upsert(self, model):
        pass
