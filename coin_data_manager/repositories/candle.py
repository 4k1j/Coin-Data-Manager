from typing import List
import psycopg2 as pg

from coin_data_manager.models.candle import Candle
from coin_data_manager.repositories.producer import NotFoundError
from coin_data_manager.repositories.repository import (
    AbstractRepository, AlreadyExistError
)
from coin_data_manager.util import CandleUnit


class CandleRepository(AbstractRepository):
    def __init__(self, database, host, port, user, password):
        self.connection = pg.connect(
            database=database, host=host, port=port, user=user, password=password,
        )

    def add(self, candle: Candle):
        try:
            cursor = self.connection.cursor()

            query = f"""
                INSERT INTO candle (market, unit, datetime, open_price, high_price, low_price, close_price, acc_trade_price, acc_trade_volume, create_datetime, update_datetime) 
                VALUES (
                    '{candle.market}',
                    '{candle.unit.value}',
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
                raise AlreadyExistError(
                    f"{candle.market} {candle.unit} {candle.datetime} already exists"
                )
            else:
                raise Exception(e)

    def delete(self, candle: Candle):
        try:
            cursor = self.connection.cursor()

            query = f"""
                DELETE FROM candle 
                WHERE market = '{candle.market}' 
                AND unit = '{candle.unit.value}'
                AND datetime::timestamp(0) = '{candle.datetime}' 
            """

            cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e

    def get(self, candle: Candle) -> Candle:
        try:
            cursor = self.connection.cursor()

            query = f"""
                SELECT market,
                    unit,
                    datetime,
                    open_price,
                    high_price,
                    low_price,
                    close_price,
                    acc_trade_price,
                    acc_trade_volume 
                FROM candle 
                WHERE market = '{candle.market}' 
                AND unit = '{candle.unit.value}'
                AND datetime::timestamp(0) = '{candle.datetime}' 
            """

            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) == 0:
                raise NotFoundError(
                    f"Not found candle : {candle.market}:{candle.unit}:{candle.datetime}"
                )

            result = result[0]

            return Candle(
                market=result[0],
                unit=CandleUnit(result[1]),
                _datetime=result[2],
                open_price=result[3],
                high_price=result[4],
                low_price=result[5],
                close_price=result[6],
                acc_trade_price=result[7],
                acc_trade_volume=result[8],
            )
        except Exception as e:
            self.connection.rollback()
            raise e


    def get_all(self) -> List[Candle]:
        pass

    def update(self, candle: Candle):
        pass

    def upsert(self, candle: Candle):
        pass

    def get_date_count(self, market):
        cursor = self.connection.cursor()

        query = f"""
            WITH candle_date AS (
                SELECT distinct GENERATE_SERIES(candle_date.start_date, candle_date.end_date, '1 day')::date as date
                FROM (
                         SELECT min(datetime) as start_date, max(datetime) as end_date FROM candle WHERE market = '{market}'
                     ) as candle_date
            ), btc_candle AS(
                SELECT * FROM candle WHERE market = '{market}'
            )

            SELECT cd.date, count(cd.date)
            FROM candle_date as cd
            LEFT JOIN btc_candle as bc
            ON cd.date = bc.datetime::date
            GROUP BY 1
            ORDER BY 1 desc
        """

        cursor.execute(query)
        results = cursor.fetchall()
        return results
