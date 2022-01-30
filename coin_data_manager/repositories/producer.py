from coin_data_manager.models.producer import Producer
from coin_data_manager.repositories.repository import AbstractRepository, NotFoundError, AlreadyExistError
from typing import List
import psycopg2 as pg

from coin_data_manager.util import CandleUnit


class ProducerRepository(AbstractRepository):
    def __init__(self, database, host, port, user, password):
        self.connection = pg.connect(
            database=database, host=host, port=port, user=user, password=password,
        )

    def delete(self, producer: Producer):
        try:
            cursor = self.connection.cursor()

            query = f"""
                DELETE FROM producer 
                WHERE market = '{producer.market}' 
                AND unit = '{producer.unit.value}'
            """
            print("delete query ", query)

            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e

    def add(self, producer: Producer):
        cursor = self.connection.cursor()

        query = f"""
        INSERT INTO producer (market, unit, heartbeat, "order")
        VALUES (
            '{producer.market}',
            '{producer.unit.value}',
            '{producer.heartbeat}',
            '{producer.order}'
        )
        """.replace(
            "'None'", "NULL"
        )

        try:
            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()

            if "already exists" in f"{e}":
                raise AlreadyExistError(
                    f"{producer} already exists"
                )

            print(f"Error query : {query}")
            raise e

    def get(self, producer) -> Producer:
        cursor = self.connection.cursor()

        query = f"""
        SELECT market, unit, heartbeat, "order"
        FROM producer
        WHERE market = '{producer.market}' and unit = '{producer.unit.value}'
        """

        cursor.execute(query)
        results = cursor.fetchall()
        if len(results) == 0:
            self.connection.rollback()
            raise NotFoundError(
                f"Not found producer : {producer.market}:{producer.unit}"
            )

        market, unit, heartbeat, order = results[0]

        return Producer(market, CandleUnit(unit), heartbeat, order)

    def get_all(self) -> List[Producer]:
        cursor = self.connection.cursor()

        query = f"""
        SELECT market, unit, heartbeat, "order"
        FROM producer
        """

        cursor.execute(query)
        results = cursor.fetchall()

        return [
            Producer(market, CandleUnit(unit), heartbeat, order)
            for market, unit, heartbeat, order in results
        ]

    def update(self, producer: Producer):
        cursor = self.connection.cursor()

        query = f"""
        UPDATE producer
        SET market = '{producer.market}',
            unit = '{producer.unit.value}',
            heartbeat = '{producer.heartbeat}',
            "order" = '{producer.order}'
        
        WHERE market = '{producer.market}' AND unit = '{producer.unit.value}'
        """.replace(
            "'None'", "NULL"
        )

        cursor.execute(query)
        self.connection.commit()

    def upsert(self, model):
        pass
