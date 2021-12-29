from typing import List
import psycopg2 as pg

from coin_data_manager.models.candle import Candle
from coin_data_manager.repositories.repository import AbstractRepository


class AlreadyExistError(Exception):
    pass


class CandleRepository(AbstractRepository):

    def __init__(self, database, host, port, user, password):
        self.connection = pg.connect(
            database=database,
            host=host,
            port=port,
            user=user,
            password=password,
        )

    def add(self, candle: Candle):
        try:
            cursor = self.connection.cursor()

            query = f"""
                INSERT INTO candle (market, unit, datetime, open_price, high_price, low_price, close_price, acc_trade_price, acc_trade_volume, create_datetime, update_datetime) 
                VALUES (
                    '{candle.market}',
                    '{candle.unit}',
                    '{candle.datetime}',
                    {candle.open_price},
                    {candle.high_price},
                    {candle.low_price},
                    {candle.close_price},
                    {candle.acc_trade_price},
                    {candle.acc_trade_volume},
                    current_timestamp,
                    current_timestamp
                )
            """

            cursor.execute(query)
            self.connection.commit()

        except Exception as e:
            self.connection.rollback()
            if "already exists" in f"{e}":
                raise AlreadyExistError(f"{candle.market} {candle.unit} {candle.datetime} already exists")
            else:
                raise Exception(e)

    def get(self, candle: Candle) -> List[Candle]:
        pass

    def get_all(self) -> List[Candle]:
        pass

    def update(self, candle: Candle):
        pass

    def upsert(self, candle: Candle):
        pass
